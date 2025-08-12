# D:\Web_AI_Temp\backend\app\config.py

class Settings:
    SQL_DRIVER = "ODBC Driver 17 for SQL Server"
    SQL_SERVER = "localhost"
    SQL_DB = "SCMESDB"
    SQL_USER = "sa"
    SQL_PWD = ")^dnjf30dlf"

    LOOKBACK_DAYS = 7     # 최근 데이터 조회일
    LSTM_LOOKBACK = 30    # LSTM 시퀀스 길이

settings = Settings()

# # D:\Web_AI_Temp\backend\app\config.py
# import os

# # 모델 경로 설정
# MODEL_PATH = os.path.join("models", "lstm_model.h5")

# # 시계열 시퀀스 길이
# SEQUENCE_LENGTH = 20

# # DB 연결 정보 (예시)
# DB_CONFIG = {
#     "driver": "ODBC Driver 17 for SQL Server",
#     "server": "localhost",
#     "database": "SCMESDB",
#     "uid": "sa",
#     "pwd": ")^dnjf30dlf",
# }


# # class Settings:
# #     SQL_DRIVER = "ODBC Driver 17 for SQL Server"
# #     SQL_SERVER = "localhost"
# #     SQL_DB = "SCMESDB"
# #     SQL_USER = "sa"
# #     SQL_PWD = ")^dnjf30dlf"
# #     MODEL_PATH = "./models/lstm_model.h5"
# #     LOOKBACK = 30  # LSTM 학습 시 사용할 시계열 길이

# # settings = Settings()
