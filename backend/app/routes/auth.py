from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import hashlib
from app.db import get_connection  

router = APIRouter()

class LoginData(BaseModel):
    user_id: str
    password: str

@router.post("/login")
async def login(data: LoginData):
    user_id = data.user_id.strip()
    password = data.password.strip()
    hashed_pw = hashlib.sha512(password.encode("utf-8")).digest()

    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="DB 연결 실패")

    try:
        cursor = conn.cursor()
        query = """
        SELECT USER_ID, USER_NAME
          FROM MSYSUSRDEF
         WHERE PLANT_ID = '01'
           AND USER_ID  = ?
           AND PASSWORD = ?
           AND USE_FLAG = 'Y'
           AND DEL_FLAG = 'N'
        """
        cursor.execute(query, (user_id, hashed_pw))
        row = cursor.fetchone()

        if row:
            return JSONResponse(
                content={"msg": "로그인 성공", "user_id": row[0], "user_name": row[1]},
                media_type="application/json; charset=utf-8",
            )
        else:
            raise HTTPException(status_code=401, detail="❌ 아이디 또는 비밀번호가 틀렸습니다.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"🔥 서버 오류: {str(e)}")
    finally:
        conn.close()
