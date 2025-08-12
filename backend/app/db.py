#db.py
import pyodbc
from contextlib import contextmanager
from typing import Any, Dict, List, Optional
from .config import settings

_CONN_STR = (
    f"DRIVER={settings.SQL_DRIVER};"
    f"SERVER={settings.SQL_SERVER};"
    f"DATABASE={settings.SQL_DB};"
    f"UID={settings.SQL_USER};PWD={settings.SQL_PWD};"
    "TrustServerCertificate=yes;"
)

@contextmanager
def get_conn():
    conn = pyodbc.connect(_CONN_STR)
    try:
        yield conn
    finally:
        conn.close()

def call_sp_fetchall(sp_name: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
    placeholders = ", ".join([f"@{k}=?" for k in params.keys()])
    sql = f"EXEC {sp_name} {placeholders}"
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(sql, list(params.values()))
        columns = [c[0] for c in cur.description] if cur.description else []
        rows = [dict(zip(columns, r)) for r in cur.fetchall()] if columns else []
    return rows

def call_sp_exec(sp_name: str, params: Dict[str, Any]) -> None:
    placeholders = ", ".join([f"@{k}=?" for k in params.keys()])
    sql = f"EXEC {sp_name} {placeholders}"
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(sql, list(params.values()))
        conn.commit()

def fetch_hour_slot_stats(plant_id: str, res_id: str, tag: str, hour_slot: str, end_dt) -> Optional[Dict[str, float]]:
    """
    최근 LOOKBACK_DAYS 동안 동일 hour_slot의 VALUE 통계(평균/표준편차) 조회
    """
    with get_conn() as conn:
        cur = conn.cursor()
        sql = """
        SELECT 
            AVG(CAST(VALUE AS FLOAT)) AS mean_val,
            STDEV(CAST(VALUE AS FLOAT)) AS std_val
        FROM dbo.AI_EQP_PREDICT_RESULT WITH (NOLOCK)
        WHERE PLANT_ID=? AND RES_ID=? AND TAG_NAME=?
          AND HOUR_SLOT=? 
          AND TRAN_TIME BETWEEN DATEADD(DAY, ?, ?) AND ?
        """
        cur.execute(sql, (plant_id, res_id, tag, hour_slot, -settings.LOOKBACK_DAYS, end_dt, end_dt))
        row = cur.fetchone()
        if not row or row[0] is None:
            return None
        mean_val = float(row[0])
        std_val = float(row[1] or 0.0)
        return {"mean": mean_val, "std": std_val}
