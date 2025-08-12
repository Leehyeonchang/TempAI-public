# D:\Web_AI_Temp\backend\app\services\ai_service.py
import numpy as np
from datetime import datetime
from keras.models import load_model
from app.utils.features import hour_slot

# 모델 로드
MODEL_PATH = "models/lstm_model.h5"
model = load_model(MODEL_PATH)

# 예측
def predict_value(observed_value: float, tran_time: datetime, meta: dict) -> float:
    # 입력 벡터 구성: [observed, hour, month]
    input_vec = np.array([[observed_value, tran_time.hour, tran_time.month]])
    input_vec = input_vec.reshape((1, 1, 3))  # (batch, time_steps, features)
    prediction = model.predict(input_vec)
    return float(prediction[0][0])

# 이상 판단 및 점수 계산
def band_and_score(mean, std, pred, observed):
    threshold = std * 2 if std else 0
    upper = (mean + threshold) if mean else 0
    lower = (mean - threshold) if mean else 0
    is_anomaly = abs(pred - mean) > threshold if mean else False
    score = abs(pred - observed) if observed is not None else 0
    return upper, lower, threshold, is_anomaly, score
