# D:\Web_AI_Temp\backend\app\main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ai_predict
#테스트용 확인
app = FastAPI(title="AI Predict API")

# CORS (필요 시 도메인 조정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(ai_predict.router, prefix="/predict", tags=["AI Predict"])

@app.get("/")
def root():
    return {"message": "✅ AI Predict API is running!"}
