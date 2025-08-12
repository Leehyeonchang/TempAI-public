# predict.py (schemas/predict.py)
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PredictRequest(BaseModel):
    plant_id: str
    res_id: str
    tag_name: str
    tran_id: Optional[str] = None  # 생략 시 최신 데이터로 예측

class PredictResponse(BaseModel):
    tran_id: str
    predict_value: float
    upper: float
    lower: float
    threshold: float
    is_anomaly: bool
    score: float
