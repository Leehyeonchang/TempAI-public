# D:\Web_AI_Temp\backend\app\services\lstm_predictor.py

import numpy as np
import pandas as pd
import joblib
import os
from keras.models import load_model
from datetime import datetime, timedelta

from app.db import call_sp_fetchall
from app.config import settings

LOOKBACK = 30  # 입력 시퀀스 길이
MODEL_PATH = "models/lstm_model.h5"
SCALER_PATH = "models/scaler.save"

# 모델과 스케일러 로딩 (최초 1회만 로딩되도록 캐싱)
_model = None
_scaler = None

def load_artifacts():
    global _model, _scaler
    if _model is None:
        _model = load_model(MODEL_PATH)
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)
    return _model, _scaler

def get_recent_sequence(plant_id: str, res_id: str, tag_name: str) -> np.ndarray:
    """
    LSTM 입력용 최근 LOOKBACK 길이의 VALUE 시퀀스 조회 (정규화 포함)
    """ 
    rows = call_sp_fetchall("usp_AI_EQP_PREDICT_S", {
        "PLANT_ID": plant_id,
        "RES_ID": res_id,
        "TAG_NAME": tag_name,
        "START_DT": datetime.utcnow() - timedelta(days=7),
        "END_DT": datetime.utcnow(),
    })
    df = pd.DataFrame(rows)
    df["TRAN_TIME"] = pd.to_datetime(df["TRAN_TIME"])
    df = df.sort_values("TRAN_TIME")
    df["VALUE"] = pd.to_numeric(df["VALUE"], errors="coerce")
    df = df.dropna(subset=["VALUE"])

    if len(df) < LOOKBACK:
        raise ValueError(f"데이터 부족: {len(df)}건")

    seq = df["VALUE"].values[-LOOKBACK:]
    return seq.reshape(-1, 1)

def predict_next_value(plant_id: str, res_id: str, tag_name: str) -> float:
    """
    지정 설비의 과거 데이터를 기반으로 향후 예측값 반환
    """
    model, scaler = load_artifacts()

    # 최근 시퀀스 조회 및 정규화
    sequence = get_recent_sequence(plant_id, res_id, tag_name)
    scaled_seq = scaler.transform(sequence)
    X = np.reshape(scaled_seq, (1, LOOKBACK, 1))

    # 예측 수행
    pred_scaled = model.predict(X, verbose=0)
    pred = scaler.inverse_transform(pred_scaled)

    return float(pred[0][0])
