# routes/ai_predict.py
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List

from app.db import call_sp_fetchall, call_sp_exec
from app.schemas.predict import PredictRunIn, PredictRunOut, PredictQuery, HistoryRow
from app.services.lstm_predictor import predict_future_value
from app.utils.features import hour_slot

router = APIRouter(prefix="/predict")  # ✅ prefix 정리

SP_SELECT = "dbo.usp_AI_EQP_PREDICT_S"
SP_UPDATE = "dbo.usp_AI_EQP_PREDICT_U"

@router.get("/history", response_model=List[HistoryRow])
def get_history(q: PredictQuery):
    rows = call_sp_fetchall(
        SP_SELECT,
        {
            "PLANT_ID": q.plant_id,
            "RES_ID": q.res_id,
            "TAG_NAME": q.tag_name,
            "START_DT": q.start_dt,
            "END_DT": q.end_dt,
        },
    )
    return rows


@router.post("/run", response_model=PredictRunOut)
def run_predict(body: PredictRunIn):
    rows = call_sp_fetchall(
        SP_SELECT,
        {
            "PLANT_ID": body.plant_id,
            "RES_ID": body.res_id,
            "TAG_NAME": body.tag_name,
            "START_DT": datetime(2000, 1, 1),
            "END_DT": datetime.utcnow(),
        },
    )
    if not rows:
        raise HTTPException(status_code=404, detail="데이터 없음")

    values = [float(r["VALUE"]) for r in rows if r.get("VALUE") is not None]
    if len(values) < 20:
        raise HTTPException(status_code=400, detail="데이터 부족 (20개 이상 필요)")

    predict_val = predict_future_value(values)
    latest = rows[0]
    observed = float(latest["VALUE"])

    mean_val = sum(values[-20:]) / 20
    std_val = (sum([(v - mean_val) ** 2 for v in values[-20:]]) / 20) ** 0.5
    threshold_val = 2 * std_val
    upper = mean_val + 3 * std_val
    lower = mean_val - 3 * std_val
    is_anom = predict_val > upper or predict_val < lower
    score = abs(observed - predict_val) / threshold_val if threshold_val else 0

    call_sp_exec(
        SP_UPDATE,
        {
            "PLANT_ID": latest["PLANT_ID"],
            "RES_ID": latest["RES_ID"],
            "TAG_NAME": latest["TAG_NAME"],
            "TRAN_ID": latest["TRAN_ID"],
            "PREDICT_VALUE": f"{predict_val:.4f}",
            "THRESHOLD_VAL": f"{threshold_val:.4f}",
            "UPPER_VAL": f"{upper:.4f}",
            "LOWER_VAL": f"{lower:.4f}",
            "IS_ANOMALY": "Y" if is_anom else "N",
            "SCORE": f"{score:.4f}",
            "ENT_USER_ID": "AI",
        },
    )

    return PredictRunOut(
        tran_id=latest["TRAN_ID"],
        observed_value=observed,
        predict_value=predict_val,
        upper=upper,
        lower=lower,
        threshold=threshold_val,
        is_anomaly=is_anom,
        score=score,
    )
