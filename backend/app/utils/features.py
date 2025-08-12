# D:\Web_AI_Temp\backend\app\utils\features.py
from datetime import datetime

def hour_slot(dt: datetime) -> str:
    """시간대(HOUR_SLOT)를 문자열로 변환"""
    return str(dt.hour).zfill(2)
