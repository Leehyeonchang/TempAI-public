#login.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import get_connection
import hashlib

router = APIRouter()

# 요청 모델
class LoginRequest(BaseModel):
    user_id: str
    password: str

# 응답 모델 (선택사항)
class LoginResponse(BaseModel):
    result: str
    user_id: str
    user_name: str

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    user_id = data.user_id
    password = data.password

    # ✅ SHA2-512 해시 생성 (바이트 배열로)
    hashed_pw = hashlib.sha512(password.encode('utf-8')).digest()

    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="🚨 데이터베이스에 연결할 수 없습니다.")

    try:
        cursor = conn.cursor()
        query = """
        SELECT USER_ID, USER_NAME
          FROM MSYSUSRDEF
         WHERE PLANT_ID  = '01'
           AND USER_ID   = ?
           AND PASSWORD  = ?
           AND USE_FLAG  = 'Y'
           AND DEL_FLAG  = 'N'
        """
        cursor.execute(query, (user_id, hashed_pw))
        row = cursor.fetchone()

        if row:
            return {
                "result": "success",
                "user_id": row[0],
                "user_name": row[1]
            }
        else:
            raise HTTPException(status_code=401, detail="❌ 아이디 또는 비밀번호가 올바르지 않습니다.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"🔥 서버 내부 오류: {str(e)}")
    finally:
        conn.close()
