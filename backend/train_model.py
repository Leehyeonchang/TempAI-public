import pandas as pd
import numpy as np
import pyodbc
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

# DB 연결 함수
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=192.168.101.93,14330;"
        "DATABASE=SCMESDB;"
        "UID=sa;"
        "PWD=)^dnjf30dlf" 
    )

# 1. 과거 데이터 불러오기
def load_data(plant_id, res_id, tag_name):
    conn = get_connection()
    query = f"""
        SELECT TOP 50000
               CONVERT(FLOAT, VALUE) AS VALUE,
               DATEPART(HOUR, TRAN_TIME) AS HOUR,
               DATEPART(MONTH, TRAN_TIME) AS MONTH
        FROM dbo.CWIPTAGDAT WITH (NOLOCK)
        WHERE PLANT_ID = '{plant_id}'
          AND RES_ID = '{res_id}'
          AND TAG_NAME = '{tag_name}'
          AND VALUE IS NOT NULL
        ORDER BY TRAN_TIME DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 2. 모델 학습
def train_model(df):
    # 특징값(X): 현재 값 + 시간(HOUR) + 월(MONTH)
    X = df[['VALUE', 'HOUR', 'MONTH']]
    # 목표값(y): 다음 시점의 값 (shift 사용)
    df['TARGET'] = df['VALUE'].shift(-1)
    df = df.dropna()

    X = df[['VALUE', 'HOUR', 'MONTH']]
    y = df['TARGET']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"✅ 모델 학습 완료 | MSE: {mse:.4f}")

    return model

# # 3. 모델 저장
# def save_model(model, filename="models/temp_predict_model.pkl"):
#     joblib.dump(model, filename)
#     print(f"✅ 모델이 저장되었습니다 → {filename}")

# 3. 모델 저장 (폴더 없으면 자동 생성)
def save_model(model, filename="models/temp_predict_model.pkl"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # 폴더 없으면 생성
    joblib.dump(model, filename)
    print(f"✅ 모델이 저장되었습니다 → {filename}")

if __name__ == "__main__":
    df = load_data("01", "59-066", "S3_TEMP")
    model = train_model(df)
    save_model(model)
