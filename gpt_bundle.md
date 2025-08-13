# GPT Bundle — TempAI-public
- Generated: 2025-08-13T14:20:23.648099Z

## Directory tree (filtered)

```
.
  .gitignore
  README.md
  gpt_bundle.md
backend
  backend/__init__.py
  backend/requirements.txt
  backend/train_model.py
backend/app
  backend/app/__init__.py
  backend/app/config.py
  backend/app/db.py
  backend/app/main.py
backend/app/schemas
  backend/app/schemas/predict.py
backend/app/services
  backend/app/services/ai_service.py
  backend/app/services/lstm_predictor.py
backend/app/routes
  backend/app/routes/__init__.py
  backend/app/routes/ai_predict.py
  backend/app/routes/auth.py
  backend/app/routes/login.py
backend/app/utils
  backend/app/utils/fcm_notify.py
  backend/app/utils/features.py
frontend
  frontend/.gitignore
  frontend/.metadata
  frontend/README.md
  frontend/analysis_options.yaml
  frontend/pubspec.lock
  frontend/pubspec.yaml
frontend/macos
  frontend/macos/.gitignore
frontend/macos/Runner
  frontend/macos/Runner/AppDelegate.swift
  frontend/macos/Runner/DebugProfile.entitlements
  frontend/macos/Runner/Info.plist
  frontend/macos/Runner/MainFlutterWindow.swift
  frontend/macos/Runner/Release.entitlements
frontend/macos/Runner/Configs
  frontend/macos/Runner/Configs/AppInfo.xcconfig
  frontend/macos/Runner/Configs/Debug.xcconfig
  frontend/macos/Runner/Configs/Release.xcconfig
  frontend/macos/Runner/Configs/Warnings.xcconfig
frontend/macos/Runner/Assets.xcassets
frontend/macos/Runner/Assets.xcassets/AppIcon.appiconset
  frontend/macos/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json
frontend/macos/Runner/Base.lproj
  frontend/macos/Runner/Base.lproj/MainMenu.xib
frontend/macos/Flutter
  frontend/macos/Flutter/Flutter-Debug.xcconfig
  frontend/macos/Flutter/Flutter-Release.xcconfig
  frontend/macos/Flutter/GeneratedPluginRegistrant.swift
frontend/macos/RunnerTests
  frontend/macos/RunnerTests/RunnerTests.swift
frontend/macos/Runner.xcodeproj
  frontend/macos/Runner.xcodeproj/project.pbxproj
frontend/macos/Runner.xcodeproj/xcshareddata
frontend/macos/Runner.xcodeproj/xcshareddata/xcschemes
  frontend/macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme
frontend/macos/Runner.xcodeproj/project.xcworkspace
frontend/macos/Runner.xcodeproj/project.xcworkspace/xcshareddata
  frontend/macos/Runner.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
frontend/macos/Runner.xcworkspace
  frontend/macos/Runner.xcworkspace/contents.xcworkspacedata
frontend/macos/Runner.xcworkspace/xcshareddata
  frontend/macos/Runner.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
frontend/windows
  frontend/windows/.gitignore
  frontend/windows/CMakeLists.txt
frontend/windows/runner
  frontend/windows/runner/CMakeLists.txt
  frontend/windows/runner/Runner.rc
  frontend/windows/runner/flutter_window.cpp
  frontend/windows/runner/flutter_window.h
  frontend/windows/runner/main.cpp
  frontend/windows/runner/resource.h
  frontend/windows/runner/runner.exe.manifest
  frontend/windows/runner/utils.cpp
  frontend/windows/runner/utils.h
  frontend/windows/runner/win32_window.cpp
  frontend/windows/runner/win32_window.h
frontend/windows/runner/resources
  frontend/windows/runner/resources/app_icon.ico
frontend/windows/flutter
  frontend/windows/flutter/CMakeLists.txt
  frontend/windows/flutter/generated_plugin_registrant.cc
  frontend/windows/flutter/generated_plugin_registrant.h
  frontend/windows/flutter/generated_plugins.cmake
frontend/android
  frontend/android/.gitignore
  frontend/android/build.gradle.kts
  frontend/android/gradle.properties
  frontend/android/settings.gradle.kts
frontend/android/app
  frontend/android/app/build.gradle.kts
frontend/android/app/src
frontend/android/app/src/profile
  frontend/android/app/src/profile/AndroidManifest.xml
frontend/android/app/src/debug
  frontend/android/app/src/debug/AndroidManifest.xml
frontend/android/app/src/main
  frontend/android/app/src/main/AndroidManifest.xml
frontend/android/app/src/main/kotlin
frontend/android/app/src/main/kotlin/com
frontend/android/app/src/main/kotlin/com/example
frontend/android/app/src/main/kotlin/com/example/frontend
  frontend/android/app/src/main/kotlin/com/example/frontend/MainActivity.kt
frontend/android/app/src/main/res
frontend/android/app/src/main/res/mipmap-xhdpi
frontend/android/app/src/main/res/mipmap-mdpi
frontend/android/app/src/main/res/drawable
  frontend/android/app/src/main/res/drawable/launch_background.xml
frontend/android/app/src/main/res/drawable-v21
  frontend/android/app/src/main/res/drawable-v21/launch_background.xml
frontend/android/app/src/main/res/mipmap-xxxhdpi
frontend/android/app/src/main/res/values-night
  frontend/android/app/src/main/res/values-night/styles.xml
frontend/android/app/src/main/res/mipmap-hdpi
frontend/android/app/src/main/res/mipmap-xxhdpi
frontend/android/app/src/main/res/values
  frontend/android/app/src/main/res/values/styles.xml
frontend/android/gradle
frontend/android/gradle/wrapper
  frontend/android/gradle/wrapper/gradle-wrapper.properties
frontend/web
  frontend/web/index.html
  frontend/web/manifest.json
frontend/web/icons
frontend/ios
  frontend/ios/.gitignore
frontend/ios/Runner
  frontend/ios/Runner/AppDelegate.swift
  frontend/ios/Runner/Info.plist
  frontend/ios/Runner/Runner-Bridging-Header.h
frontend/ios/Runner/Assets.xcassets
frontend/ios/Runner/Assets.xcassets/AppIcon.appiconset
  frontend/ios/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json
frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset
  frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset/Contents.json
  frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset/README.md
frontend/ios/Runner/Base.lproj
  frontend/ios/Runner/Base.lproj/LaunchScreen.storyboard
  frontend/ios/Runner/Base.lproj/Main.storyboard
frontend/ios/Flutter
  frontend/ios/Flutter/AppFrameworkInfo.plist
  frontend/ios/Flutter/Debug.xcconfig
  frontend/ios/Flutter/Release.xcconfig
frontend/ios/RunnerTests
  frontend/ios/RunnerTests/RunnerTests.swift
frontend/ios/Runner.xcodeproj
  frontend/ios/Runner.xcodeproj/project.pbxproj
frontend/ios/Runner.xcodeproj/xcshareddata
frontend/ios/Runner.xcodeproj/xcshareddata/xcschemes
  frontend/ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme
frontend/ios/Runner.xcodeproj/project.xcworkspace
  frontend/ios/Runner.xcodeproj/project.xcworkspace/contents.xcworkspacedata
frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata
  frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
  frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings
frontend/ios/Runner.xcworkspace
  frontend/ios/Runner.xcworkspace/contents.xcworkspacedata
frontend/ios/Runner.xcworkspace/xcshareddata
  frontend/ios/Runner.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
  frontend/ios/Runner.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings
frontend/test
  frontend/test/widget_test.dart
frontend/lib
  frontend/lib/main.dart
frontend/lib/screens
  frontend/lib/screens/ai_monitor.dart
  frontend/lib/screens/home_screen.dart
  frontend/lib/screens/login_screen.dart
frontend/lib/screens/menu
  frontend/lib/screens/menu/ai_home_menu.dart
  frontend/lib/screens/menu/anomaly_screen.dart
  frontend/lib/screens/menu/histogram_screen.dart
  frontend/lib/screens/menu/trend_screen.dart
frontend/lib/services
  frontend/lib/services/api_service.dart
frontend/linux
  frontend/linux/.gitignore
  frontend/linux/CMakeLists.txt
frontend/linux/runner
  frontend/linux/runner/CMakeLists.txt
  frontend/linux/runner/main.cc
  frontend/linux/runner/my_application.cc
  frontend/linux/runner/my_application.h
frontend/linux/flutter
  frontend/linux/flutter/CMakeLists.txt
  frontend/linux/flutter/generated_plugin_registrant.cc
  frontend/linux/flutter/generated_plugin_registrant.h
  frontend/linux/flutter/generated_plugins.cmake
frontend/assets
frontend/assets/logo
.github
.github/workflows
  .github/workflows/make_gpt_bundle.yml
.github/tools
  .github/tools/gpt_repo_bundler.py
```

## Files (truncated)

### `.gitignore`
`size: 6 bytes`

```
venv/

```

### `README.md`
`size: 1577 bytes`

```md
# TempAI (public mirror)

자동 생성된 공개 미러입니다. 비밀/대용량 파일은 제외됩니다.

## Structure
```
.
./pub
./pub/pub
./pub/backend
./pub/frontend
./backend
./backend/app
./backend/app/schemas
./backend/app/services
./backend/app/routes
./backend/app/utils
./frontend
./frontend/macos
./frontend/macos/Runner
./frontend/macos/Runner/Configs
./frontend/macos/Runner/Assets.xcassets
./frontend/macos/Runner/Base.lproj
./frontend/macos/Flutter
./frontend/macos/RunnerTests
./frontend/macos/Runner.xcodeproj
./frontend/macos/Runner.xcodeproj/xcshareddata
./frontend/macos/Runner.xcodeproj/project.xcworkspace
./frontend/macos/Runner.xcworkspace
./frontend/macos/Runner.xcworkspace/xcshareddata
./frontend/windows
./frontend/windows/runner
./frontend/windows/runner/resources
./frontend/windows/flutter
./frontend/android
./frontend/android/app
./frontend/android/app/src
./frontend/android/gradle
./frontend/android/gradle/wrapper
./frontend/web
./frontend/web/icons
./frontend/ios
./frontend/ios/Runner
./frontend/ios/Runner/Assets.xcassets
./frontend/ios/Runner/Base.lproj
./frontend/ios/Flutter
./frontend/ios/RunnerTests
./frontend/ios/Runner.xcodeproj
./frontend/ios/Runner.xcodeproj/xcshareddata
./frontend/ios/Runner.xcodeproj/project.xcworkspace
./frontend/ios/Runner.xcworkspace
./frontend/ios/Runner.xcworkspace/xcshareddata
./frontend/test
./frontend/lib
./frontend/lib/screens
./frontend/lib/screens/menu
./frontend/lib/services
./frontend/linux
./frontend/linux/runner
./frontend/linux/flutter
./frontend/assets
./frontend/assets/logo
```

```

### `gpt_bundle.md`
`size: 9707 bytes`

```md
# GPT Bundle — TempAI-public
- Generated: 2025-08-13T14:20:23.648099Z

## Directory tree (filtered)

```
.
  .gitignore
  README.md
  gpt_bundle.md
backend
  backend/__init__.py
  backend/requirements.txt
  backend/train_model.py
backend/app
  backend/app/__init__.py
  backend/app/config.py
  backend/app/db.py
  backend/app/main.py
backend/app/schemas
  backend/app/schemas/predict.py
backend/app/services
  backend/app/services/ai_service.py
  backend/app/services/lstm_predictor.py
backend/app/routes
  backend/app/routes/__init__.py
  backend/app/routes/ai_predict.py
  backend/app/routes/auth.py
  backend/app/routes/login.py
backend/app/utils
  backend/app/utils/fcm_notify.py
  backend/app/utils/features.py
frontend
  frontend/.gitignore
  frontend/.metadata
  frontend/README.md
  frontend/analysis_options.yaml
  frontend/pubspec.lock
  frontend/pubspec.yaml
frontend/macos
  frontend/macos/.gitignore
frontend/macos/Runner
  frontend/macos/Runner/AppDelegate.swift
  frontend/macos/Runner/DebugProfile.entitlements
  frontend/macos/Runner/Info.plist
  frontend/macos/Runner/MainFlutterWindow.swift
  frontend/macos/Runner/Release.entitlements
frontend/macos/Runner/Configs
  frontend/macos/Runner/Configs/AppInfo.xcconfig
  frontend/macos/Runner/Configs/Debug.xcconfig
  frontend/macos/Runner/Configs/Release.xcconfig
  frontend/macos/Runner/Configs/Warnings.xcconfig
frontend/macos/Runner/Assets.xcassets
frontend/macos/Runner/Assets.xcassets/AppIcon.appiconset
  frontend/macos/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json
frontend/macos/Runner/Base.lproj
  frontend/macos/Runner/Base.lproj/MainMenu.xib
frontend/macos/Flutter
  frontend/macos/Flutter/Flutter-Debug.xcconfig
  frontend/macos/Flutter/Flutter-Release.xcconfig
  frontend/macos/Flutter/GeneratedPluginRegistrant.swift
frontend/macos/RunnerTests
  frontend/macos/RunnerTests/RunnerTests.swift
frontend/macos/Runner.xcodeproj
  frontend/macos/Runner.xcodeproj/project.pbxproj
frontend/macos/Runner.xcodeproj/xcshareddata
frontend/macos/Runner.xcodeproj/xcshareddata/xcschemes
  frontend/macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme
frontend/macos/Runner.xcodeproj/project.xcworkspace
frontend/macos/Runner.xcodeproj/project.xcworkspace/xcshareddata
  frontend/macos/Runner.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
frontend/macos/Runner.xcworkspace
  frontend/macos/Runner.xcworkspace/contents.xcworkspacedata
frontend/macos/Runner.xcworkspace/xcshareddata
  frontend/macos/Runner.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
frontend/windows
  frontend/windows/.gitignore
  frontend/windows/CMakeLists.txt
frontend/windows/runner
  frontend/windows/runner/CMakeLists.txt
  frontend/windows/runner/Runner.rc
  frontend/windows/runner/flutter_window.cpp
  frontend/windows/runner/flutter_window.h
  frontend/windows/runner/main.cpp
  frontend/windows/runner/resource.h
  frontend/windows/runner/runner.exe.manifest
  frontend/windows/runner/utils.cpp
  frontend/windows/runner/utils.h
  frontend/windows/runner/win32_window.cpp
  frontend/windows/runner/win32_window.h
frontend/windows/runner/resources
  frontend/windows/runner/resources/app_icon.ico
frontend/windows/flutter
  frontend/windows/flutter/CMakeLists.txt
  frontend/windows/flutter/generated_plugin_registrant.cc
  frontend/windows/flutter/generated_plugin_registrant.h
  frontend/windows/flutter/generated_plugins.cmake
frontend/android
  frontend/android/.gitignore
  frontend/android/build.gradle.kts
  frontend/android/gradle.properties
  frontend/android/settings.gradle.kts
frontend/android/app
  frontend/android/app/build.gradle.kts
frontend/android/app/src
frontend/android/app/src/profile
  frontend/android/app/src/profile/AndroidManifest.xml
frontend/android/app/src/debug
  frontend/android/app/src/debug/AndroidManifest.xml
frontend/android/app/src/main
  frontend/android/app/src/main/AndroidManifest.xml
frontend/android/app/src/main/kotlin
frontend/android/app/src/main/kotlin/com
frontend/android/app/src/main/kotlin/com/example
frontend/android/app/src/main/kotlin/com/example/frontend
  frontend/android/app/src/main/kotlin/com/example/frontend/MainActivity.kt
frontend/android/app/src/main/res
frontend/android/app/src/main/res/mipmap-xhdpi
frontend/android/app/src/main/res/mipmap-mdpi
frontend/android/app/src/main/res/drawable
  frontend/android/app/src/main/res/drawable/launch_background.xml
frontend/android/app/src/main/res/drawable-v21
  frontend/android/app/src/main/res/drawable-v21/launch_background.xml
frontend/android/app/src/main/res/mipmap-xxxhdpi
frontend/android/app/src/main/res/values-night
  frontend/android/app/src/main/res/values-night/styles.xml
frontend/android/app/src/main/res/mipmap-hdpi
frontend/android/app/src/main/res/mipmap-xxhdpi
frontend/android/app/src/main/res/values
  frontend/android/app/src/main/res/values/styles.xml
frontend/android/gradle
frontend/android/gradle/wrapper
  frontend/android/gradle/wrapper/gradle-wrapper.properties
frontend/web
  frontend/web/index.html
  frontend/web/manifest.json
frontend/web/icons
frontend/ios
  frontend/ios/.gitignore
frontend/ios/Runner
  frontend/ios/Runner/AppDelegate.swift
  frontend/ios/Runner/Info.plist
  frontend/ios/Runner/Runner-Bridging-Header.h
frontend/ios/Runner/Assets.xcassets
frontend/ios/Runner/Assets.xcassets/AppIcon.appiconset
  frontend/ios/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json
frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset
  frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset/Contents.json
  frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset/README.md
frontend/ios/Runner/Base.lproj
  frontend/ios/Runner/Base.lproj/LaunchScreen.storyboard
  frontend/ios/Runner/Base.lproj/Main.storyboard
frontend/ios/Flutter
  frontend/ios/Flutter/AppFrameworkInfo.plist
  frontend/ios/Flutter/Debug.xcconfig
  frontend/ios/Flutter/Release.xcconfig
frontend/ios/RunnerTests
  frontend/ios/RunnerTests/RunnerTests.swift
frontend/ios/Runner.xcodeproj
  frontend/ios/Runner.xcodeproj/project.pbxproj
frontend/ios/Runner.xcodeproj/xcshareddata
frontend/ios/Runner.xcodeproj/xcshareddata/xcschemes
  frontend/ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme
frontend/ios/Runner.xcodeproj/project.xcworkspace
  frontend/ios/Runner.xcodeproj/project.xcworkspace/contents.xcworkspacedata
frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata
  frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
  frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings
frontend/ios/Runner.xcworkspace
  frontend/ios/Runner.xcworkspace/contents.xcworkspacedata
frontend/ios/Runner.xcworkspace/xcshareddata
  frontend/ios/Runner.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist
  frontend/ios/Runner.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings
frontend/test
  frontend/test/widget_test.dart
frontend/lib
  frontend/lib/main.dart
frontend/lib/screens
  frontend/lib/screens/ai_monitor.dart
  frontend/lib/screens/home_screen.dart
  frontend/lib/screens/login_screen.dart
frontend/lib/screens/menu
  frontend/lib/screens/menu/ai_home_menu.dart
  frontend/lib/screens/menu/anomaly_screen.dart
  frontend/lib/screens/menu/histogram_screen.dart
  frontend/lib/screens/menu/trend_screen.dart
frontend/lib/services
  frontend/lib/services/api_service.dart
frontend/linux
  frontend/linux/.gitignore
  frontend/linux/CMakeLists.txt
frontend/linux/runner
  frontend/linux/runner/CMakeLists.txt
  frontend/linux/runner/main.cc
  frontend/linux/runner/my_application.cc
  frontend/linux/runner/my_application.h
frontend/linux/flutter
  frontend/linux/flutter/CMakeLists.txt
  frontend/linux/flutter/generated_plugin_registrant.cc
  frontend/linux/flutter/generated_plugin_registrant.h
  frontend/linux/flutter/generated_plugins.cmake
frontend/assets
frontend/assets/logo
.github
.github/workflows
  .github/workflows/make_gpt_bundle.yml
.github/tools
  .github/tools/gpt_repo_bundler.py
```

## Files (truncated)

### `.gitignore`
`size: 6 bytes`

```
venv/

```

### `README.md`
`size: 1577 bytes`

```md
# TempAI (public mirror)

자동 생성된 공개 미러입니다. 비밀/대용량 파일은 제외됩니다.

## Structure
```
.
./pub
./pub/pub
./pub/backend
./pub/frontend
./backend
./backend/app
./backend/app/schemas
./backend/app/services
./backend/app/routes
./backend/app/utils
./frontend
./frontend/macos
./frontend/macos/Runner
./frontend/macos/Runner/Configs
./frontend/macos/Runner/Assets.xcassets
./frontend/macos/Runner/Base.lproj
./frontend/macos/Flutter
./frontend/macos/RunnerTests
./frontend/macos/Runner.xcodeproj
./frontend/macos/Runner.xcodeproj/xcshareddata
./frontend/macos/Runner.xcodeproj/project.xcworkspace
./frontend/macos/Runner.xcworkspace
./frontend/macos/Runner.xcworkspace/xcshareddata
./frontend/windows
./frontend/windows/runner
./frontend/windows/runner/resources
./frontend/windows/flutter
./frontend/android
./frontend/android/app
./frontend/android/app/src
./frontend/android/gradle
./frontend/android/gradle/wrapper
./frontend/web
./frontend/web/icons
./frontend/ios
./frontend/ios/Runner
./frontend/ios/Runner/Assets.xcassets
./frontend/ios/Runner/Base.lproj
./frontend/ios/Flutter
./frontend/ios/RunnerTests
./frontend/ios/Runner.xcodeproj
./frontend/ios/Runner.xcodeproj/xcshareddata
./frontend/ios/Runner.xcodeproj/project.xcworkspace
./frontend/ios/Runner.xcworkspace
./frontend/ios/Runner.xcworkspace/xcshareddata
./frontend/test
./frontend/lib
./frontend/lib/screens
./frontend/lib/screens/menu
./frontend/lib/services
./frontend/linux
./frontend/linux/runner
./frontend/linux/flutter
./frontend/assets
./frontend/assets/logo
```

```

### `backend/__init__.py`
`size: 0 bytes`

```py

```

### `backend/requirements.txt`
`size: 120 bytes`

```txt
fastapi==0.110.0
uvicorn==0.27.0
python-multipart
pandas
numpy
scikit-learn
matplotlib
pyodbc
joblib
tensorflow==2.15.0

```

### `backend/train_model.py`
`size: 2298 bytes`

```py
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

```

### `backend/app/__init__.py`
`size: 0 bytes`

```py

```

### `backend/app/config.py`
`size: 1061 bytes`

```py
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

```

### `backend/app/db.py`
`size: 2192 bytes`

```py
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

```

### `backend/app/main.py`
`size: 574 bytes`

```py
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

```

### `backend/app/schemas/predict.py`
`size: 454 bytes`

```py
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

```

### `backend/app/services/ai_service.py`
`size: 1036 bytes`

```py
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

```

### `backend/app/services/lstm_predictor.py`
`size: 2051 bytes`

```py
# D:\Web_AI_Temp\backend\app\services\lstm_predictor.py

import numpy as np
import pandas as pd
import joblib
import os
from keras.models import load_model
from datetime import datetime, timedelta

from app.db import call_sp_fetchall
from app.config import settings

LOOKBACK = 30  # 입력 시퀀스 길이
MODEL_PATH = "models/lstm_model.h5"
SCALER_PATH = "models/scaler.save"

# 모델과 스케일러 로딩 (최초 1회만 로딩되도록 캐싱)
_model = None
_scaler = None

def load_artifacts():
    global _model, _scaler
    if _model is None:
        _model = load_model(MODEL_PATH)
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)
    return _model, _scaler

def get_recent_sequence(plant_id: str, res_id: str, tag_name: str) -> np.ndarray:
    """
    LSTM 입력용 최근 LOOKBACK 길이의 VALUE 시퀀스 조회 (정규화 포함)
    """ 
    rows = call_sp_fetchall("usp_AI_EQP_PREDICT_S", {
        "PLANT_ID": plant_id,
        "RES_ID": res_id,
        "TAG_NAME": tag_name,
        "START_DT": datetime.utcnow() - timedelta(days=7),
        "END_DT": datetime.utcnow(),
    })
    df = pd.DataFrame(rows)
    df["TRAN_TIME"] = pd.to_datetime(df["TRAN_TIME"])
    df = df.sort_values("TRAN_TIME")
    df["VALUE"] = pd.to_numeric(df["VALUE"], errors="coerce")
    df = df.dropna(subset=["VALUE"])

    if len(df) < LOOKBACK:
        raise ValueError(f"데이터 부족: {len(df)}건")

    seq = df["VALUE"].values[-LOOKBACK:]
    return seq.reshape(-1, 1)

def predict_next_value(plant_id: str, res_id: str, tag_name: str) -> float:
    """
    지정 설비의 과거 데이터를 기반으로 향후 예측값 반환
    """
    model, scaler = load_artifacts()

    # 최근 시퀀스 조회 및 정규화
    sequence = get_recent_sequence(plant_id, res_id, tag_name)
    scaled_seq = scaler.transform(sequence)
    X = np.reshape(scaled_seq, (1, LOOKBACK, 1))

    # 예측 수행
    pred_scaled = model.predict(X, verbose=0)
    pred = scaler.inverse_transform(pred_scaled)

    return float(pred[0][0])

```

### `backend/app/routes/__init__.py`
`size: 0 bytes`

```py

```

### `backend/app/routes/ai_predict.py`
`size: 2770 bytes`

```py
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

```

### `backend/app/routes/auth.py`
`size: 1430 bytes`

```py
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

```

### `backend/app/routes/login.py`
`size: 1599 bytes`

```py
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

```

### `backend/app/utils/fcm_notify.py`
`size: 448 bytes`

```py
import requests

FCM_KEY = "서버_KEY_입력"
FCM_URL = "https://fcm.googleapis.com/fcm/send"

def send_push_notification(token, title, message):
    headers = {
        "Authorization": f"key={FCM_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": token,
        "notification": {
            "title": title,
            "body": message
        }
    }
    requests.post(FCM_URL, json=payload, headers=headers)

```

### `backend/app/utils/features.py`
`size: 201 bytes`

```py
# D:\Web_AI_Temp\backend\app\utils\features.py
from datetime import datetime

def hour_slot(dt: datetime) -> str:
    """시간대(HOUR_SLOT)를 문자열로 변환"""
    return str(dt.hour).zfill(2)

```

### `frontend/.gitignore`
`size: 709 bytes`

```
# Miscellaneous
*.class
*.log
*.pyc
*.swp
.DS_Store
.atom/
.build/
.buildlog/
.history
.svn/
.swiftpm/
migrate_working_dir/

# IntelliJ related
*.iml
*.ipr
*.iws
.idea/

# The .vscode folder contains launch configuration and tasks you configure in
# VS Code which you may wish to be included in version control, so this line
# is commented out by default.
#.vscode/

# Flutter/Dart/Pub related
**/doc/api/
**/ios/Flutter/.last_build_id
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
.pub-cache/
.pub/
/build/

# Symbolication related
app.*.symbols

# Obfuscation related
app.*.map.json

# Android Studio will place build artifacts here
/android/app/debug
/android/app/profile
/android/app/release

```

### `frontend/.metadata`
`size: 1706 bytes`

```
# This file tracks properties of this Flutter project.
# Used by Flutter tool to assess capabilities and perform upgrades etc.
#
# This file should be version controlled and should not be manually edited.

version:
  revision: "077b4a4ce10a07b82caa6897f0c626f9c0a3ac90"
  channel: "stable"

project_type: app

# Tracks metadata for the flutter migrate command
migration:
  platforms:
    - platform: root
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
    - platform: android
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
    - platform: ios
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
    - platform: linux
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
    - platform: macos
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
    - platform: web
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
    - platform: windows
      create_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90
      base_revision: 077b4a4ce10a07b82caa6897f0c626f9c0a3ac90

  # User provided section

  # List of Local paths (relative to this file) that should be
  # ignored by the migrate tool.
  #
  # Files that are not part of the templates will be ignored by default.
  unmanaged_files:
    - 'lib/main.dart'
    - 'ios/Runner.xcodeproj/project.pbxproj'

```

### `frontend/README.md`
`size: 551 bytes`

```md
# frontend

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

```

### `frontend/analysis_options.yaml`
`size: 1420 bytes`

```yaml
# This file configures the analyzer, which statically analyzes Dart code to
# check for errors, warnings, and lints.
#
# The issues identified by the analyzer are surfaced in the UI of Dart-enabled
# IDEs (https://dart.dev/tools#ides-and-editors). The analyzer can also be
# invoked from the command line by running `flutter analyze`.

# The following line activates a set of recommended lints for Flutter apps,
# packages, and plugins designed to encourage good coding practices.
include: package:flutter_lints/flutter.yaml

linter:
  # The lint rules applied to this project can be customized in the
  # section below to disable rules from the `package:flutter_lints/flutter.yaml`
  # included above or to enable additional rules. A list of all available lints
  # and their documentation is published at https://dart.dev/lints.
  #
  # Instead of disabling a lint rule for the entire project in the
  # section below, it can also be suppressed for a single line of code
  # or a specific dart file by using the `// ignore: name_of_lint` and
  # `// ignore_for_file: name_of_lint` syntax on the line or in the file
  # producing the lint.
  rules:
    # avoid_print: false  # Uncomment to disable the `avoid_print` rule
    # prefer_single_quotes: true  # Uncomment to enable the `prefer_single_quotes` rule

# Additional information about this file can be found at
# https://dart.dev/guides/language/analysis-options

```

### `frontend/pubspec.lock`
`size: 11549 bytes`

```lock
# Generated by pub
# See https://dart.dev/tools/pub/glossary#lockfile
packages:
  async:
    dependency: transitive
    description:
      name: async
      sha256: "758e6d74e971c3e5aceb4110bfd6698efc7f501675bcfe0c775459a8140750eb"
      url: "https://pub.dev"
    source: hosted
    version: "2.13.0"
  boolean_selector:
    dependency: transitive
    description:
      name: boolean_selector
      sha256: "8aab1771e1243a5063b8b0ff68042d67334e3feab9e95b9490f9a6ebf73b42ea"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.2"
  characters:
    dependency: transitive
    description:
      name: characters
      sha256: f71061c654a3380576a52b451dd5532377954cf9dbd272a78fc8479606670803
      url: "https://pub.dev"
    source: hosted
    version: "1.4.0"
  clock:
    dependency: transitive
    description:
      name: clock
      sha256: fddb70d9b5277016c77a80201021d40a2247104d9f4aa7bab7157b7e3f05b84b
      url: "https://pub.dev"
    source: hosted
    version: "1.1.2"
  collection:
    dependency: transitive
    description:
      name: collection
      sha256: "2f5709ae4d3d59dd8f7cd309b4e023046b57d8a6c82130785d2b0e5868084e76"
      url: "https://pub.dev"
    source: hosted
    version: "1.19.1"
  cupertino_icons:
    dependency: "direct main"
    description:
      name: cupertino_icons
      sha256: ba631d1c7f7bef6b729a622b7b752645a2d076dba9976925b8f25725a30e1ee6
      url: "https://pub.dev"
    source: hosted
    version: "1.0.8"
  easy_sidemenu:
    dependency: "direct main"
    description:
      name: easy_sidemenu
      sha256: "591cabac129822c0c89a7e16607a9a45ffec58f21fbac1228db93abbf7010eff"
      url: "https://pub.dev"
    source: hosted
    version: "0.6.1"
  equatable:
    dependency: transitive
    description:
      name: equatable
      sha256: "567c64b3cb4cf82397aac55f4f0cbd3ca20d77c6c03bedbc4ceaddc08904aef7"
      url: "https://pub.dev"
    source: hosted
    version: "2.0.7"
  fake_async:
    dependency: transitive
    description:
      name: fake_async
      sha256: "5368f224a74523e8d2e7399ea1638b37aecfca824a3cc4dfdf77bf1fa905ac44"
      url: "https://pub.dev"
    source: hosted
    version: "1.3.3"
  ffi:
    dependency: transitive
    description:
      name: ffi
      sha256: "289279317b4b16eb2bb7e271abccd4bf84ec9bdcbe999e278a94b804f5630418"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.4"
  file:
    dependency: transitive
    description:
      name: file
      sha256: a3b4f84adafef897088c160faf7dfffb7696046cb13ae90b508c2cbc95d3b8d4
      url: "https://pub.dev"
    source: hosted
    version: "7.0.1"
  fl_chart:
    dependency: "direct main"
    description:
      name: fl_chart
      sha256: d0f0d49112f2f4b192481c16d05b6418bd7820e021e265a3c22db98acf7ed7fb
      url: "https://pub.dev"
    source: hosted
    version: "0.68.0"
  flutter:
    dependency: "direct main"
    description: flutter
    source: sdk
    version: "0.0.0"
  flutter_lints:
    dependency: "direct dev"
    description:
      name: flutter_lints
      sha256: "9e8c3858111da373efc5aa341de011d9bd23e2c5c5e0c62bccf32438e192d7b1"
      url: "https://pub.dev"
    source: hosted
    version: "3.0.2"
  flutter_test:
    dependency: "direct dev"
    description: flutter
    source: sdk
    version: "0.0.0"
  flutter_web_plugins:
    dependency: transitive
    description: flutter
    source: sdk
    version: "0.0.0"
  http:
    dependency: "direct main"
    description:
      name: http
      sha256: "2c11f3f94c687ee9bad77c171151672986360b2b001d109814ee7140b2cf261b"
      url: "https://pub.dev"
    source: hosted
    version: "1.4.0"
  http_parser:
    dependency: transitive
    description:
      name: http_parser
      sha256: "178d74305e7866013777bab2c3d8726205dc5a4dd935297175b19a23a2e66571"
      url: "https://pub.dev"
    source: hosted
    version: "4.1.2"
  leak_tracker:
    dependency: transitive
    description:
      name: leak_tracker
      sha256: "6bb818ecbdffe216e81182c2f0714a2e62b593f4a4f13098713ff1685dfb6ab0"
      url: "https://pub.dev"
    source: hosted
    version: "10.0.9"
  leak_tracker_flutter_testing:
    dependency: transitive
    description:
      name: leak_tracker_flutter_testing
      sha256: f8b613e7e6a13ec79cfdc0e97638fddb3ab848452eff057653abd3edba760573
      url: "https://pub.dev"
    source: hosted
    version: "3.0.9"
  leak_tracker_testing:
    dependency: transitive
    description:
      name: leak_tracker_testing
      sha256: "6ba465d5d76e67ddf503e1161d1f4a6bc42306f9d66ca1e8f079a47290fb06d3"
      url: "https://pub.dev"
    source: hosted
    version: "3.0.1"
  lints:
    dependency: transitive
    description:
      name: lints
      sha256: cbf8d4b858bb0134ef3ef87841abdf8d63bfc255c266b7bf6b39daa1085c4290
      url: "https://pub.dev"
    source: hosted
    version: "3.0.0"
  matcher:
    dependency: transitive
    description:
      name: matcher
      sha256: dc58c723c3c24bf8d3e2d3ad3f2f9d7bd9cf43ec6feaa64181775e60190153f2
      url: "https://pub.dev"
    source: hosted
    version: "0.12.17"
  material_color_utilities:
    dependency: transitive
    description:
      name: material_color_utilities
      sha256: f7142bb1154231d7ea5f96bc7bde4bda2a0945d2806bb11670e30b850d56bdec
      url: "https://pub.dev"
    source: hosted
    version: "0.11.1"
  meta:
    dependency: transitive
    description:
      name: meta
      sha256: e3641ec5d63ebf0d9b41bd43201a66e3fc79a65db5f61fc181f04cd27aab950c
      url: "https://pub.dev"
    source: hosted
    version: "1.16.0"
  path:
    dependency: transitive
    description:
      name: path
      sha256: "75cca69d1490965be98c73ceaea117e8a04dd21217b37b292c9ddbec0d955bc5"
      url: "https://pub.dev"
    source: hosted
    version: "1.9.1"
  path_provider_linux:
    dependency: transitive
    description:
      name: path_provider_linux
      sha256: f7a1fe3a634fe7734c8d3f2766ad746ae2a2884abe22e241a8b301bf5cac3279
      url: "https://pub.dev"
    source: hosted
    version: "2.2.1"
  path_provider_platform_interface:
    dependency: transitive
    description:
      name: path_provider_platform_interface
      sha256: "88f5779f72ba699763fa3a3b06aa4bf6de76c8e5de842cf6f29e2e06476c2334"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.2"
  path_provider_windows:
    dependency: transitive
    description:
      name: path_provider_windows
      sha256: bd6f00dbd873bfb70d0761682da2b3a2c2fccc2b9e84c495821639601d81afe7
      url: "https://pub.dev"
    source: hosted
    version: "2.3.0"
  platform:
    dependency: transitive
    description:
      name: platform
      sha256: "5d6b1b0036a5f331ebc77c850ebc8506cbc1e9416c27e59b439f917a902a4984"
      url: "https://pub.dev"
    source: hosted
    version: "3.1.6"
  plugin_platform_interface:
    dependency: transitive
    description:
      name: plugin_platform_interface
      sha256: "4820fbfdb9478b1ebae27888254d445073732dae3d6ea81f0b7e06d5dedc3f02"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.8"
  shared_preferences:
    dependency: "direct main"
    description:
      name: shared_preferences
      sha256: "6e8bf70b7fef813df4e9a36f658ac46d107db4b4cfe1048b477d4e453a8159f5"
      url: "https://pub.dev"
    source: hosted
    version: "2.5.3"
  shared_preferences_android:
    dependency: transitive
    description:
      name: shared_preferences_android
      sha256: "20cbd561f743a342c76c151d6ddb93a9ce6005751e7aa458baad3858bfbfb6ac"
      url: "https://pub.dev"
    source: hosted
    version: "2.4.10"
  shared_preferences_foundation:
    dependency: transitive
    description:
      name: shared_preferences_foundation
      sha256: "6a52cfcdaeac77cad8c97b539ff688ccfc458c007b4db12be584fbe5c0e49e03"
      url: "https://pub.dev"
    source: hosted
    version: "2.5.4"
  shared_preferences_linux:
    dependency: transitive
    description:
      name: shared_preferences_linux
      sha256: "580abfd40f415611503cae30adf626e6656dfb2f0cee8f465ece7b6defb40f2f"
      url: "https://pub.dev"
    source: hosted
    version: "2.4.1"
  shared_preferences_platform_interface:
    dependency: transitive
    description:
      name: shared_preferences_platform_interface
      sha256: "57cbf196c486bc2cf1f02b85784932c6094376284b3ad5779d1b1c6c6a816b80"
      url: "https://pub.dev"
    source: hosted
    version: "2.4.1"
  shared_preferences_web:
    dependency: transitive
    description:
      name: shared_preferences_web
      sha256: c49bd060261c9a3f0ff445892695d6212ff603ef3115edbb448509d407600019
      url: "https://pub.dev"
    source: hosted
    version: "2.4.3"
  shared_preferences_windows:
    dependency: transitive
    description:
      name: shared_preferences_windows
      sha256: "94ef0f72b2d71bc3e700e025db3710911bd51a71cefb65cc609dd0d9a982e3c1"
      url: "https://pub.dev"
    source: hosted
    version: "2.4.1"
  sky_engine:
    dependency: transitive
    description: flutter
    source: sdk
    version: "0.0.0"
  source_span:
    dependency: transitive
    description:
      name: source_span
      sha256: "254ee5351d6cb365c859e20ee823c3bb479bf4a293c22d17a9f1bf144ce86f7c"
      url: "https://pub.dev"
    source: hosted
    version: "1.10.1"
  stack_trace:
    dependency: transitive
    description:
      name: stack_trace
      sha256: "8b27215b45d22309b5cddda1aa2b19bdfec9df0e765f2de506401c071d38d1b1"
      url: "https://pub.dev"
    source: hosted
    version: "1.12.1"
  stream_channel:
    dependency: transitive
    description:
      name: stream_channel
      sha256: "969e04c80b8bcdf826f8f16579c7b14d780458bd97f56d107d3950fdbeef059d"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.4"
  string_scanner:
    dependency: transitive
    description:
      name: string_scanner
      sha256: "921cd31725b72fe181906c6a94d987c78e3b98c2e205b397ea399d4054872b43"
      url: "https://pub.dev"
    source: hosted
    version: "1.4.1"
  term_glyph:
    dependency: transitive
    description:
      name: term_glyph
      sha256: "7f554798625ea768a7518313e58f83891c7f5024f88e46e7182a4558850a4b8e"
      url: "https://pub.dev"
    source: hosted
    version: "1.2.2"
  test_api:
    dependency: transitive
    description:
      name: test_api
      sha256: fb31f383e2ee25fbbfe06b40fe21e1e458d14080e3c67e7ba0acfde4df4e0bbd
      url: "https://pub.dev"
    source: hosted
    version: "0.7.4"
  typed_data:
    dependency: transitive
    description:
      name: typed_data
      sha256: f9049c039ebfeb4cf7a7104a675823cd72dba8297f264b6637062516699fa006
      url: "https://pub.dev"
    source: hosted
    version: "1.4.0"
  vector_math:
    dependency: transitive
    description:
      name: vector_math
      sha256: "80b3257d1492ce4d091729e3a67a60407d227c27241d6927be0130c98e741803"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.4"
  vm_service:
    dependency: transitive
    description:
      name: vm_service
      sha256: ddfa8d30d89985b96407efce8acbdd124701f96741f2d981ca860662f1c0dc02
      url: "https://pub.dev"
    source: hosted
    version: "15.0.0"
  web:
    dependency: transitive
    description:
      name: web
      sha256: "868d88a33d8a87b18ffc05f9f030ba328ffefba92d6c127917a2ba740f9cfe4a"
      url: "https://pub.dev"
    source: hosted
    version: "1.1.1"
  xdg_directories:
    dependency: transitive
    description:
      name: xdg_directories
      sha256: "7a3f37b05d989967cdddcbb571f1ea834867ae2faa29725fd085180e0883aa15"
      url: "https://pub.dev"
    source: hosted
    version: "1.1.0"
sdks:
  dart: ">=3.7.0 <4.0.0"
  flutter: ">=3.27.0"

```

### `frontend/pubspec.yaml`
`size: 628 bytes`

```yaml
name: frontend
description: "AI 예측 및 이상 감지 Flutter 앱"
publish_to: "none"

version: 1.0.0+1

environment:
  sdk: ">=3.0.0 <4.0.0"  # 안정적인 범위로 수정

dependencies:
  flutter:
    sdk: flutter

  # ✅ 네트워크 요청
  http: ^1.2.0  

  # ✅ 자동 로그인용
  shared_preferences: ^2.2.2  

  # ✅ 사이드 메뉴
  easy_sidemenu: ^0.6.0  

  # ✅ 그래프 시각화
  fl_chart: ^0.68.0  

  # ✅ 아이콘
  cupertino_icons: ^1.0.8

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1

flutter:
  uses-material-design: true

  assets:
    - assets/logo/CH_2.png

```

### `frontend/macos/.gitignore`
`size: 89 bytes`

```
# Flutter-related
**/Flutter/ephemeral/
**/Pods/

# Xcode-related
**/dgph
**/xcuserdata/

```

### `frontend/macos/Runner/AppDelegate.swift`
`size: 311 bytes`

```swift
import Cocoa
import FlutterMacOS

@main
class AppDelegate: FlutterAppDelegate {
  override func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
    return true
  }

  override func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool {
    return true
  }
}

```

### `frontend/macos/Runner/DebugProfile.entitlements`
`size: 348 bytes`

```entitlements
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.cs.allow-jit</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
</dict>
</plist>

```

### `frontend/macos/Runner/Info.plist`
`size: 1060 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>$(DEVELOPMENT_LANGUAGE)</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIconFile</key>
	<string></string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>$(PRODUCT_NAME)</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>$(FLUTTER_BUILD_NAME)</string>
	<key>CFBundleVersion</key>
	<string>$(FLUTTER_BUILD_NUMBER)</string>
	<key>LSMinimumSystemVersion</key>
	<string>$(MACOSX_DEPLOYMENT_TARGET)</string>
	<key>NSHumanReadableCopyright</key>
	<string>$(PRODUCT_COPYRIGHT)</string>
	<key>NSMainNibFile</key>
	<string>MainMenu</string>
	<key>NSPrincipalClass</key>
	<string>NSApplication</string>
</dict>
</plist>

```

### `frontend/macos/Runner/MainFlutterWindow.swift`
`size: 388 bytes`

```swift
import Cocoa
import FlutterMacOS

class MainFlutterWindow: NSWindow {
  override func awakeFromNib() {
    let flutterViewController = FlutterViewController()
    let windowFrame = self.frame
    self.contentViewController = flutterViewController
    self.setFrame(windowFrame, display: true)

    RegisterGeneratedPlugins(registry: flutterViewController)

    super.awakeFromNib()
  }
}

```

### `frontend/macos/Runner/Release.entitlements`
`size: 240 bytes`

```entitlements
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### `frontend/macos/Runner/Configs/AppInfo.xcconfig`
`size: 603 bytes`

```xcconfig
// Application-level settings for the Runner target.
//
// This may be replaced with something auto-generated from metadata (e.g., pubspec.yaml) in the
// future. If not, the values below would default to using the project name when this becomes a
// 'flutter create' template.

// The application's name. By default this is also the title of the Flutter window.
PRODUCT_NAME = frontend

// The application's bundle identifier
PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend

// The copyright displayed in application information
PRODUCT_COPYRIGHT = Copyright © 2025 com.example. All rights reserved.

```

### `frontend/macos/Runner/Configs/Debug.xcconfig`
`size: 77 bytes`

```xcconfig
#include "../../Flutter/Flutter-Debug.xcconfig"
#include "Warnings.xcconfig"

```

### `frontend/macos/Runner/Configs/Release.xcconfig`
`size: 79 bytes`

```xcconfig
#include "../../Flutter/Flutter-Release.xcconfig"
#include "Warnings.xcconfig"

```

### `frontend/macos/Runner/Configs/Warnings.xcconfig`
`size: 580 bytes`

```xcconfig
WARNING_CFLAGS = -Wall -Wconditional-uninitialized -Wnullable-to-nonnull-conversion -Wmissing-method-return-type -Woverlength-strings
GCC_WARN_UNDECLARED_SELECTOR = YES
CLANG_UNDEFINED_BEHAVIOR_SANITIZER_NULLABILITY = YES
CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE
CLANG_WARN__DUPLICATE_METHOD_MATCH = YES
CLANG_WARN_PRAGMA_PACK = YES
CLANG_WARN_STRICT_PROTOTYPES = YES
CLANG_WARN_COMMA = YES
GCC_WARN_STRICT_SELECTOR_MATCH = YES
CLANG_WARN_OBJC_REPEATED_USE_OF_WEAK = YES
CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES
GCC_WARN_SHADOW = YES
CLANG_WARN_UNREACHABLE_CODE = YES

```

### `frontend/macos/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json`
`size: 1291 bytes`

```json
{
  "images" : [
    {
      "size" : "16x16",
      "idiom" : "mac",
      "filename" : "app_icon_16.png",
      "scale" : "1x"
    },
    {
      "size" : "16x16",
      "idiom" : "mac",
      "filename" : "app_icon_32.png",
      "scale" : "2x"
    },
    {
      "size" : "32x32",
      "idiom" : "mac",
      "filename" : "app_icon_32.png",
      "scale" : "1x"
    },
    {
      "size" : "32x32",
      "idiom" : "mac",
      "filename" : "app_icon_64.png",
      "scale" : "2x"
    },
    {
      "size" : "128x128",
      "idiom" : "mac",
      "filename" : "app_icon_128.png",
      "scale" : "1x"
    },
    {
      "size" : "128x128",
      "idiom" : "mac",
      "filename" : "app_icon_256.png",
      "scale" : "2x"
    },
    {
      "size" : "256x256",
      "idiom" : "mac",
      "filename" : "app_icon_256.png",
      "scale" : "1x"
    },
    {
      "size" : "256x256",
      "idiom" : "mac",
      "filename" : "app_icon_512.png",
      "scale" : "2x"
    },
    {
      "size" : "512x512",
      "idiom" : "mac",
      "filename" : "app_icon_512.png",
      "scale" : "1x"
    },
    {
      "size" : "512x512",
      "idiom" : "mac",
      "filename" : "app_icon_1024.png",
      "scale" : "2x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}

```

### `frontend/macos/Runner/Base.lproj/MainMenu.xib`
`size: 23729 bytes`

```xib
<?xml version="1.0" encoding="UTF-8"?>
<document type="com.apple.InterfaceBuilder3.Cocoa.XIB" version="3.0" toolsVersion="14490.70" targetRuntime="MacOSX.Cocoa" propertyAccessControl="none" useAutolayout="YES" customObjectInstantitationMethod="direct">
    <dependencies>
        <deployment identifier="macosx"/>
        <plugIn identifier="com.apple.InterfaceBuilder.CocoaPlugin" version="14490.70"/>
        <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
    </dependencies>
    <objects>
        <customObject id="-2" userLabel="File's Owner" customClass="NSApplication">
            <connections>
                <outlet property="delegate" destination="Voe-Tx-rLC" id="GzC-gU-4Uq"/>
            </connections>
        </customObject>
        <customObject id="-1" userLabel="First Responder" customClass="FirstResponder"/>
        <customObject id="-3" userLabel="Application" customClass="NSObject"/>
        <customObject id="Voe-Tx-rLC" customClass="AppDelegate" customModule="Runner" customModuleProvider="target">
            <connections>
                <outlet property="applicationMenu" destination="uQy-DD-JDr" id="XBo-yE-nKs"/>
                <outlet property="mainFlutterWindow" destination="QvC-M9-y7g" id="gIp-Ho-8D9"/>
            </connections>
        </customObject>
        <customObject id="YLy-65-1bz" customClass="NSFontManager"/>
        <menu title="Main Menu" systemMenu="main" id="AYu-sK-qS6">
            <items>
                <menuItem title="APP_NAME" id="1Xt-HY-uBw">
                    <modifierMask key="keyEquivalentModifierMask"/>
                    <menu key="submenu" title="APP_NAME" systemMenu="apple" id="uQy-DD-JDr">
                        <items>
                            <menuItem title="About APP_NAME" id="5kV-Vb-QxS">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <connections>
                                    <action selector="orderFrontStandardAboutPanel:" target="-1" id="Exp-CZ-Vem"/>
                                </connections>
                            </menuItem>
                            <menuItem isSeparatorItem="YES" id="VOq-y0-SEH"/>
                            <menuItem title="Preferences…" keyEquivalent="," id="BOF-NM-1cW"/>
                            <menuItem isSeparatorItem="YES" id="wFC-TO-SCJ"/>
                            <menuItem title="Services" id="NMo-om-nkz">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <menu key="submenu" title="Services" systemMenu="services" id="hz9-B4-Xy5"/>
                            </menuItem>
                            <menuItem isSeparatorItem="YES" id="4je-JR-u6R"/>
                            <menuItem title="Hide APP_NAME" keyEquivalent="h" id="Olw-nP-bQN">
                                <connections>
                                    <action selector="hide:" target="-1" id="PnN-Uc-m68"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Hide Others" keyEquivalent="h" id="Vdr-fp-XzO">
                                <modifierMask key="keyEquivalentModifierMask" option="YES" command="YES"/>
                                <connections>
                                    <action selector="hideOtherApplications:" target="-1" id="VT4-aY-XCT"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Show All" id="Kd2-mp-pUS">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <connections>
                                    <action selector="unhideAllApplications:" target="-1" id="Dhg-Le-xox"/>
                                </connections>
                            </menuItem>
                            <menuItem isSeparatorItem="YES" id="kCx-OE-vgT"/>
                            <menuItem title="Quit APP_NAME" keyEquivalent="q" id="4sb-4s-VLi">
                                <connections>
                                    <action selector="terminate:" target="-1" id="Te7-pn-YzF"/>
                                </connections>
                            </menuItem>
                        </items>
                    </menu>
                </menuItem>
                <menuItem title="Edit" id="5QF-Oa-p0T">
                    <modifierMask key="keyEquivalentModifierMask"/>
                    <menu key="submenu" title="Edit" id="W48-6f-4Dl">
                        <items>
                            <menuItem title="Undo" keyEquivalent="z" id="dRJ-4n-Yzg">
                                <connections>
                                    <action selector="undo:" target="-1" id="M6e-cu-g7V"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Redo" keyEquivalent="Z" id="6dh-zS-Vam">
                                <connections>
                                    <action selector="redo:" target="-1" id="oIA-Rs-6OD"/>
                                </connections>
                            </menuItem>
                            <menuItem isSeparatorItem="YES" id="WRV-NI-Exz"/>
                            <menuItem title="Cut" keyEquivalent="x" id="uRl-iY-unG">
                                <connections>
                                    <action selector="cut:" target="-1" id="YJe-68-I9s"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Copy" keyEquivalent="c" id="x3v-GG-iWU">
                                <connections>
                                    <action selector="copy:" target="-1" id="G1f-GL-Joy"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Paste" keyEquivalent="v" id="gVA-U4-sdL">
                                <connections>
                                    <action selector="paste:" target="-1" id="UvS-8e-Qdg"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Paste and Match Style" keyEquivalent="V" id="WeT-3V-zwk">
                                <modifierMask key="keyEquivalentModifierMask" option="YES" command="YES"/>
                                <connections>
                                    <action selector="pasteAsPlainText:" target="-1" id="cEh-KX-wJQ"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Delete" id="pa3-QI-u2k">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <connections>
                                    <action selector="delete:" target="-1" id="0Mk-Ml-PaM"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Select All" keyEquivalent="a" id="Ruw-6m-B2m">
                                <connections>
                                    <action selector="selectAll:" target="-1" id="VNm-Mi-diN"/>
                                </connections>
                            </menuItem>
                            <menuItem isSeparatorItem="YES" id="uyl-h8-XO2"/>
                            <menuItem title="Find" id="4EN-yA-p0u">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <menu key="submenu" title="Find" id="1b7-l0-nxx">
                                    <items>
                                        <menuItem title="Find…" tag="1" keyEquivalent="f" id="Xz5-n4-O0W">
                                            <connections>
                                                <action selector="performFindPanelAction:" target="-1" id="cD7-Qs-BN4"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Find and Replace…" tag="12" keyEquivalent="f" id="YEy-JH-Tfz">
                                            <modifierMask key="keyEquivalentModifierMask" option="YES" command="YES"/>
                                            <connections>
                                                <action selector="performFindPanelAction:" target="-1" id="WD3-Gg-5AJ"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Find Next" tag="2" keyEquivalent="g" id="q09-fT-Sye">
                                            <connections>
                                                <action selector="performFindPanelAction:" target="-1" id="NDo-RZ-v9R"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Find Previous" tag="3" keyEquivalent="G" id="OwM-mh-QMV">
                                            <connections>
                                                <action selector="performFindPanelAction:" target="-1" id="HOh-sY-3ay"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Use Selection for Find" tag="7" keyEquivalent="e" id="buJ-ug-pKt">
                                            <connections>
                                                <action selector="performFindPanelAction:" target="-1" id="U76-nv-p5D"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Jump to Selection" keyEquivalent="j" id="S0p-oC-mLd">
                                            <connections>
                                                <action selector="centerSelectionInVisibleArea:" target="-1" id="IOG-6D-g5B"/>
                                            </connections>
                                        </menuItem>
                                    </items>
                                </menu>
                            </menuItem>
                            <menuItem title="Spelling and Grammar" id="Dv1-io-Yv7">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <menu key="submenu" title="Spelling" id="3IN-sU-3Bg">
                                    <items>
                                        <menuItem title="Show Spelling and Grammar" keyEquivalent=":" id="HFo-cy-zxI">
                                            <connections>
                                                <action selector="showGuessPanel:" target="-1" id="vFj-Ks-hy3"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Check Document Now" keyEquivalent=";" id="hz2-CU-CR7">
                                            <connections>
                                                <action selector="checkSpelling:" target="-1" id="fz7-VC-reM"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem isSeparatorItem="YES" id="bNw-od-mp5"/>
                                        <menuItem title="Check Spelling While Typing" id="rbD-Rh-wIN">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleContinuousSpellChecking:" target="-1" id="7w6-Qz-0kB"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Check Grammar With Spelling" id="mK6-2p-4JG">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleGrammarChecking:" target="-1" id="muD-Qn-j4w"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Correct Spelling Automatically" id="78Y-hA-62v">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleAutomaticSpellingCorrection:" target="-1" id="2lM-Qi-WAP"/>
                                            </connections>
                                        </menuItem>
                                    </items>
                                </menu>
                            </menuItem>
                            <menuItem title="Substitutions" id="9ic-FL-obx">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <menu key="submenu" title="Substitutions" id="FeM-D8-WVr">
                                    <items>
                                        <menuItem title="Show Substitutions" id="z6F-FW-3nz">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="orderFrontSubstitutionsPanel:" target="-1" id="oku-mr-iSq"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem isSeparatorItem="YES" id="gPx-C9-uUO"/>
                                        <menuItem title="Smart Copy/Paste" id="9yt-4B-nSM">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleSmartInsertDelete:" target="-1" id="3IJ-Se-DZD"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Smart Quotes" id="hQb-2v-fYv">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleAutomaticQuoteSubstitution:" target="-1" id="ptq-xd-QOA"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Smart Dashes" id="rgM-f4-ycn">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleAutomaticDashSubstitution:" target="-1" id="oCt-pO-9gS"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Smart Links" id="cwL-P1-jid">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleAutomaticLinkDetection:" target="-1" id="Gip-E3-Fov"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Data Detectors" id="tRr-pd-1PS">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleAutomaticDataDetection:" target="-1" id="R1I-Nq-Kbl"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Text Replacement" id="HFQ-gK-NFA">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="toggleAutomaticTextReplacement:" target="-1" id="DvP-Fe-Py6"/>
                                            </connections>
                                        </menuItem>
                                    </items>
                                </menu>
                            </menuItem>
                            <menuItem title="Transformations" id="2oI-Rn-ZJC">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <menu key="submenu" title="Transformations" id="c8a-y6-VQd">
                                    <items>
                                        <menuItem title="Make Upper Case" id="vmV-6d-7jI">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="uppercaseWord:" target="-1" id="sPh-Tk-edu"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Make Lower Case" id="d9M-CD-aMd">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="lowercaseWord:" target="-1" id="iUZ-b5-hil"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Capitalize" id="UEZ-Bs-lqG">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="capitalizeWord:" target="-1" id="26H-TL-nsh"/>
                                            </connections>
                                        </menuItem>
                                    </items>
                                </menu>
                            </menuItem>
                            <menuItem title="Speech" id="xrE-MZ-jX0">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <menu key="submenu" title="Speech" id="3rS-ZA-NoH">
                                    <items>
                                        <menuItem title="Start Speaking" id="Ynk-f8-cLZ">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="startSpeaking:" target="-1" id="654-Ng-kyl"/>
                                            </connections>
                                        </menuItem>
                                        <menuItem title="Stop Speaking" id="Oyz-dy-DGm">
                                            <modifierMask key="keyEquivalentModifierMask"/>
                                            <connections>
                                                <action selector="stopSpeaking:" target="-1" id="dX8-6p-jy9"/>
                                            </connections>
                                        </menuItem>
                                    </items>
                                </menu>
                            </menuItem>
                        </items>
                    </menu>
                </menuItem>
                <menuItem title="View" id="H8h-7b-M4v">
                    <modifierMask key="keyEquivalentModifierMask"/>
                    <menu key="submenu" title="View" id="HyV-fh-RgO">
                        <items>
                            <menuItem title="Enter Full Screen" keyEquivalent="f" id="4J7-dP-txa">
                                <modifierMask key="keyEquivalentModifierMask" control="YES" command="YES"/>
                                <connections>
                                    <action selector="toggleFullScreen:" target="-1" id="dU3-MA-1Rq"/>
                                </connections>
                            </menuItem>
                        </items>
                    </menu>
                </menuItem>
                <menuItem title="Window" id="aUF-d1-5bR">
                    <modifierMask key="keyEquivalentModifierMask"/>
                    <menu key="submenu" title="Window" systemMenu="window" id="Td7-aD-5lo">
                        <items>
                            <menuItem title="Minimize" keyEquivalent="m" id="OY7-WF-poV">
                                <connections>
                                    <action selector="performMiniaturize:" target="-1" id="VwT-WD-YPe"/>
                                </connections>
                            </menuItem>
                            <menuItem title="Zoom" id="R4o-n2-Eq4">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <connections>
                                    <action selector="performZoom:" target="-1" id="DIl-cC-cCs"/>
                                </connections>
                            </menuItem>
                            <menuItem isSeparatorItem="YES" id="eu3-7i-yIM"/>
                            <menuItem title="Bring All to Front" id="LE2-aR-0XJ">
                                <modifierMask key="keyEquivalentModifierMask"/>
                                <connections>
                                    <action selector="arrangeInFront:" target="-1" id="DRN-fu-gQh"/>
                                </connections>
                            </menuItem>
                        </items>
                    </menu>
                </menuItem>
                <menuItem title="Help" id="EPT-qC-fAb">
                    <modifierMask key="keyEquivalentModifierMask"/>
                    <menu key="submenu" title="Help" systemMenu="help" id="rJ0-wn-3NY"/>
                </menuItem>
            </items>
            <point key="canvasLocation" x="142" y="-258"/>
        </menu>
        <window title="APP_NAME" allowsToolTipsWhenApplicationIsInactive="NO" autorecalculatesKeyViewLoop="NO" releasedWhenClosed="NO" animationBehavior="default" id="QvC-M9-y7g" customClass="MainFlutterWindow" customModule="Runner" customModuleProvider="target">
            <windowStyleMask key="styleMask" titled="YES" closable="YES" miniaturizable="YES" resizable="YES"/>
            <rect key="contentRect" x="335" y="390" width="800" height="600"/>
            <rect key="screenRect" x="0.0" y="0.0" width="2560" height="1577"/>
            <view key="contentView" wantsLayer="YES" id="EiT-Mj-1SZ">
                <rect key="frame" x="0.0" y="0.0" width="800" height="600"/>
                <autoresizingMask key="autoresizingMask"/>
            </view>
        </window>
    </objects>
</document>

```

### `frontend/macos/Flutter/Flutter-Debug.xcconfig`
`size: 48 bytes`

```xcconfig
#include "ephemeral/Flutter-Generated.xcconfig"

```

### `frontend/macos/Flutter/Flutter-Release.xcconfig`
`size: 48 bytes`

```xcconfig
#include "ephemeral/Flutter-Generated.xcconfig"

```

### `frontend/macos/Flutter/GeneratedPluginRegistrant.swift`
`size: 283 bytes`

```swift
//
//  Generated file. Do not edit.
//

import FlutterMacOS
import Foundation

import shared_preferences_foundation

func RegisterGeneratedPlugins(registry: FlutterPluginRegistry) {
  SharedPreferencesPlugin.register(with: registry.registrar(forPlugin: "SharedPreferencesPlugin"))
}

```

### `frontend/macos/RunnerTests/RunnerTests.swift`
`size: 290 bytes`

```swift
import Cocoa
import FlutterMacOS
import XCTest

class RunnerTests: XCTestCase {

  func testExample() {
    // If you add code to the Runner application, consider adding tests here.
    // See https://developer.apple.com/documentation/xctest for more information about using XCTest.
  }

}

```

### `frontend/macos/Runner.xcodeproj/project.pbxproj`
`size: 26359 bytes`

```pbxproj
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 54;
	objects = {

/* Begin PBXAggregateTarget section */
		33CC111A2044C6BA0003C045 /* Flutter Assemble */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = 33CC111B2044C6BA0003C045 /* Build configuration list for PBXAggregateTarget "Flutter Assemble" */;
			buildPhases = (
				33CC111E2044C6BF0003C045 /* ShellScript */,
			);
			dependencies = (
			);
			name = "Flutter Assemble";
			productName = FLX;
		};
/* End PBXAggregateTarget section */

/* Begin PBXBuildFile section */
		331C80D8294CF71000263BE5 /* RunnerTests.swift in Sources */ = {isa = PBXBuildFile; fileRef = 331C80D7294CF71000263BE5 /* RunnerTests.swift */; };
		335BBD1B22A9A15E00E9071D /* GeneratedPluginRegistrant.swift in Sources */ = {isa = PBXBuildFile; fileRef = 335BBD1A22A9A15E00E9071D /* GeneratedPluginRegistrant.swift */; };
		33CC10F12044A3C60003C045 /* AppDelegate.swift in Sources */ = {isa = PBXBuildFile; fileRef = 33CC10F02044A3C60003C045 /* AppDelegate.swift */; };
		33CC10F32044A3C60003C045 /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 33CC10F22044A3C60003C045 /* Assets.xcassets */; };
		33CC10F62044A3C60003C045 /* MainMenu.xib in Resources */ = {isa = PBXBuildFile; fileRef = 33CC10F42044A3C60003C045 /* MainMenu.xib */; };
		33CC11132044BFA00003C045 /* MainFlutterWindow.swift in Sources */ = {isa = PBXBuildFile; fileRef = 33CC11122044BFA00003C045 /* MainFlutterWindow.swift */; };
/* End PBXBuildFile section */

/* Begin PBXContainerItemProxy section */
		331C80D9294CF71000263BE5 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = 33CC10E52044A3C60003C045 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = 33CC10EC2044A3C60003C045;
			remoteInfo = Runner;
		};
		33CC111F2044C79F0003C045 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = 33CC10E52044A3C60003C045 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = 33CC111A2044C6BA0003C045;
			remoteInfo = FLX;
		};
/* End PBXContainerItemProxy section */

/* Begin PBXCopyFilesBuildPhase section */
		33CC110E2044A8840003C045 /* Bundle Framework */ = {
			isa = PBXCopyFilesBuildPhase;
			buildActionMask = 2147483647;
			dstPath = "";
			dstSubfolderSpec = 10;
			files = (
			);
			name = "Bundle Framework";
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXCopyFilesBuildPhase section */

/* Begin PBXFileReference section */
		331C80D5294CF71000263BE5 /* RunnerTests.xctest */ = {isa = PBXFileReference; explicitFileType = wrapper.cfbundle; includeInIndex = 0; path = RunnerTests.xctest; sourceTree = BUILT_PRODUCTS_DIR; };
		331C80D7294CF71000263BE5 /* RunnerTests.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RunnerTests.swift; sourceTree = "<group>"; };
		333000ED22D3DE5D00554162 /* Warnings.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; path = Warnings.xcconfig; sourceTree = "<group>"; };
		335BBD1A22A9A15E00E9071D /* GeneratedPluginRegistrant.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = GeneratedPluginRegistrant.swift; sourceTree = "<group>"; };
		33CC10ED2044A3C60003C045 /* frontend.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = "frontend.app"; sourceTree = BUILT_PRODUCTS_DIR; };
		33CC10F02044A3C60003C045 /* AppDelegate.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AppDelegate.swift; sourceTree = "<group>"; };
		33CC10F22044A3C60003C045 /* Assets.xcassets */ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; name = Assets.xcassets; path = Runner/Assets.xcassets; sourceTree = "<group>"; };
		33CC10F52044A3C60003C045 /* Base */ = {isa = PBXFileReference; lastKnownFileType = file.xib; name = Base; path = Base.lproj/MainMenu.xib; sourceTree = "<group>"; };
		33CC10F72044A3C60003C045 /* Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; name = Info.plist; path = Runner/Info.plist; sourceTree = "<group>"; };
		33CC11122044BFA00003C045 /* MainFlutterWindow.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MainFlutterWindow.swift; sourceTree = "<group>"; };
		33CEB47222A05771004F2AC0 /* Flutter-Debug.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; path = "Flutter-Debug.xcconfig"; sourceTree = "<group>"; };
		33CEB47422A05771004F2AC0 /* Flutter-Release.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; path = "Flutter-Release.xcconfig"; sourceTree = "<group>"; };
		33CEB47722A0578A004F2AC0 /* Flutter-Generated.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; name = "Flutter-Generated.xcconfig"; path = "ephemeral/Flutter-Generated.xcconfig"; sourceTree = "<group>"; };
		33E51913231747F40026EE4D /* DebugProfile.entitlements */ = {isa = PBXFileReference; lastKnownFileType = text.plist.entitlements; path = DebugProfile.entitlements; sourceTree = "<group>"; };
		33E51914231749380026EE4D /* Release.entitlements */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.entitlements; path = Release.entitlements; sourceTree = "<group>"; };
		33E5194F232828860026EE4D /* AppInfo.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; path = AppInfo.xcconfig; sourceTree = "<group>"; };
		7AFA3C8E1D35360C0083082E /* Release.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; path = Release.xcconfig; sourceTree = "<group>"; };
		9740EEB21CF90195004384FC /* Debug.xcconfig */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.xcconfig; path = Debug.xcconfig; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		331C80D2294CF70F00263BE5 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		33CC10EA2044A3C60003C045 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		331C80D6294CF71000263BE5 /* RunnerTests */ = {
			isa = PBXGroup;
			children = (
				331C80D7294CF71000263BE5 /* RunnerTests.swift */,
			);
			path = RunnerTests;
			sourceTree = "<group>";
		};
		33BA886A226E78AF003329D5 /* Configs */ = {
			isa = PBXGroup;
			children = (
				33E5194F232828860026EE4D /* AppInfo.xcconfig */,
				9740EEB21CF90195004384FC /* Debug.xcconfig */,
				7AFA3C8E1D35360C0083082E /* Release.xcconfig */,
				333000ED22D3DE5D00554162 /* Warnings.xcconfig */,
			);
			path = Configs;
			sourceTree = "<group>";
		};
		33CC10E42044A3C60003C045 = {
			isa = PBXGroup;
			children = (
				33FAB671232836740065AC1E /* Runner */,
				33CEB47122A05771004F2AC0 /* Flutter */,
				331C80D6294CF71000263BE5 /* RunnerTests */,
				33CC10EE2044A3C60003C045 /* Products */,
				D73912EC22F37F3D000D13A0 /* Frameworks */,
			);
			sourceTree = "<group>";
		};
		33CC10EE2044A3C60003C045 /* Products */ = {
			isa = PBXGroup;
			children = (
				33CC10ED2044A3C60003C045 /* frontend.app */,
				331C80D5294CF71000263BE5 /* RunnerTests.xctest */,
			);
			name = Products;
			sourceTree = "<group>";
		};
		33CC11242044D66E0003C045 /* Resources */ = {
			isa = PBXGroup;
			children = (
				33CC10F22044A3C60003C045 /* Assets.xcassets */,
				33CC10F42044A3C60003C045 /* MainMenu.xib */,
				33CC10F72044A3C60003C045 /* Info.plist */,
			);
			name = Resources;
			path = ..;
			sourceTree = "<group>";
		};
		33CEB47122A05771004F2AC0 /* Flutter */ = {
			isa = PBXGroup;
			children = (
				335BBD1A22A9A15E00E9071D /* GeneratedPluginRegistrant.swift */,
				33CEB47222A05771004F2AC0 /* Flutter-Debug.xcconfig */,
				33CEB47422A05771004F2AC0 /* Flutter-Release.xcconfig */,
				33CEB47722A0578A004F2AC0 /* Flutter-Generated.xcconfig */,
			);
			path = Flutter;
			sourceTree = "<group>";
		};
		33FAB671232836740065AC1E /* Runner */ = {
			isa = PBXGroup;
			children = (
				33CC10F02044A3C60003C045 /* AppDelegate.swift */,
				33CC11122044BFA00003C045 /* MainFlutterWindow.swift */,
				33E51913231747F40026EE4D /* DebugProfile.entitlements */,
				33E51914231749380026EE4D /* Release.entitlements */,
				33CC11242044D66E0003C045 /* Resources */,
				33BA886A226E78AF003329D5 /* Configs */,
			);
			path = Runner;
			sourceTree = "<group>";
		};
		D73912EC22F37F3D000D13A0 /* Frameworks */ = {
			isa = PBXGroup;
			children = (
			);
			name = Frameworks;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		331C80D4294CF70F00263BE5 /* RunnerTests */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 331C80DE294CF71000263BE5 /* Build configuration list for PBXNativeTarget "RunnerTests" */;
			buildPhases = (
				331C80D1294CF70F00263BE5 /* Sources */,
				331C80D2294CF70F00263BE5 /* Frameworks */,
				331C80D3294CF70F00263BE5 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
				331C80DA294CF71000263BE5 /* PBXTargetDependency */,
			);
			name = RunnerTests;
			productName = RunnerTests;
			productReference = 331C80D5294CF71000263BE5 /* RunnerTests.xctest */;
			productType = "com.apple.product-type.bundle.unit-test";
		};
		33CC10EC2044A3C60003C045 /* Runner */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 33CC10FB2044A3C60003C045 /* Build configuration list for PBXNativeTarget "Runner" */;
			buildPhases = (
				33CC10E92044A3C60003C045 /* Sources */,
				33CC10EA2044A3C60003C045 /* Frameworks */,
				33CC10EB2044A3C60003C045 /* Resources */,
				33CC110E2044A8840003C045 /* Bundle Framework */,
				3399D490228B24CF009A79C7 /* ShellScript */,
			);
			buildRules = (
			);
			dependencies = (
				33CC11202044C79F0003C045 /* PBXTargetDependency */,
			);
			name = Runner;
			productName = Runner;
			productReference = 33CC10ED2044A3C60003C045 /* frontend.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		33CC10E52044A3C60003C045 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = YES;
				LastSwiftUpdateCheck = 0920;
				LastUpgradeCheck = 1510;
				ORGANIZATIONNAME = "";
				TargetAttributes = {
					331C80D4294CF70F00263BE5 = {
						CreatedOnToolsVersion = 14.0;
						TestTargetID = 33CC10EC2044A3C60003C045;
					};
					33CC10EC2044A3C60003C045 = {
						CreatedOnToolsVersion = 9.2;
						LastSwiftMigration = 1100;
						ProvisioningStyle = Automatic;
						SystemCapabilities = {
							com.apple.Sandbox = {
								enabled = 1;
							};
						};
					};
					33CC111A2044C6BA0003C045 = {
						CreatedOnToolsVersion = 9.2;
						ProvisioningStyle = Manual;
					};
				};
			};
			buildConfigurationList = 33CC10E82044A3C60003C045 /* Build configuration list for PBXProject "Runner" */;
			compatibilityVersion = "Xcode 9.3";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 33CC10E42044A3C60003C045;
			productRefGroup = 33CC10EE2044A3C60003C045 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				33CC10EC2044A3C60003C045 /* Runner */,
				331C80D4294CF70F00263BE5 /* RunnerTests */,
				33CC111A2044C6BA0003C045 /* Flutter Assemble */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		331C80D3294CF70F00263BE5 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		33CC10EB2044A3C60003C045 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				33CC10F32044A3C60003C045 /* Assets.xcassets in Resources */,
				33CC10F62044A3C60003C045 /* MainMenu.xib in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXShellScriptBuildPhase section */
		3399D490228B24CF009A79C7 /* ShellScript */ = {
			isa = PBXShellScriptBuildPhase;
			alwaysOutOfDate = 1;
			buildActionMask = 2147483647;
			files = (
			);
			inputFileListPaths = (
			);
			inputPaths = (
			);
			outputFileListPaths = (
			);
			outputPaths = (
			);
			runOnlyForDeploymentPostprocessing = 0;
			shellPath = /bin/sh;
			shellScript = "echo \"$PRODUCT_NAME.app\" > \"$PROJECT_DIR\"/Flutter/ephemeral/.app_filename && \"$FLUTTER_ROOT\"/packages/flutter_tools/bin/macos_assemble.sh embed\n";
		};
		33CC111E2044C6BF0003C045 /* ShellScript */ = {
			isa = PBXShellScriptBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			inputFileListPaths = (
				Flutter/ephemeral/FlutterInputs.xcfilelist,
			);
			inputPaths = (
				Flutter/ephemeral/tripwire,
			);
			outputFileListPaths = (
				Flutter/ephemeral/FlutterOutputs.xcfilelist,
			);
			outputPaths = (
			);
			runOnlyForDeploymentPostprocessing = 0;
			shellPath = /bin/sh;
			shellScript = "\"$FLUTTER_ROOT\"/packages/flutter_tools/bin/macos_assemble.sh && touch Flutter/ephemeral/tripwire";
		};
/* End PBXShellScriptBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		331C80D1294CF70F00263BE5 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				331C80D8294CF71000263BE5 /* RunnerTests.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		33CC10E92044A3C60003C045 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				33CC11132044BFA00003C045 /* MainFlutterWindow.swift in Sources */,
				33CC10F12044A3C60003C045 /* AppDelegate.swift in Sources */,
				335BBD1B22A9A15E00E9071D /* GeneratedPluginRegistrant.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin PBXTargetDependency section */
		331C80DA294CF71000263BE5 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = 33CC10EC2044A3C60003C045 /* Runner */;
			targetProxy = 331C80D9294CF71000263BE5 /* PBXContainerItemProxy */;
		};
		33CC11202044C79F0003C045 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = 33CC111A2044C6BA0003C045 /* Flutter Assemble */;
			targetProxy = 33CC111F2044C79F0003C045 /* PBXContainerItemProxy */;
		};
/* End PBXTargetDependency section */

/* Begin PBXVariantGroup section */
		33CC10F42044A3C60003C045 /* MainMenu.xib */ = {
			isa = PBXVariantGroup;
			children = (
				33CC10F52044A3C60003C045 /* Base */,
			);
			name = MainMenu.xib;
			path = Runner;
			sourceTree = "<group>";
		};
/* End PBXVariantGroup section */

/* Begin XCBuildConfiguration section */
		331C80DB294CF71000263BE5 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend.RunnerTests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_VERSION = 5.0;
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/frontend.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/frontend";
			};
			name = Debug;
		};
		331C80DC294CF71000263BE5 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend.RunnerTests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_VERSION = 5.0;
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/frontend.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/frontend";
			};
			name = Release;
		};
		331C80DD294CF71000263BE5 /* Profile */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend.RunnerTests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_VERSION = 5.0;
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/frontend.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/frontend";
			};
			name = Profile;
		};
		338D0CE9231458BD00FA5F75 /* Profile */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 7AFA3C8E1D35360C0083082E /* Release.xcconfig */;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CODE_SIGN_IDENTITY = "-";
				COPY_PHASE_STRIP = NO;
				DEAD_CODE_STRIPPING = YES;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = NO;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				MACOSX_DEPLOYMENT_TARGET = 10.14;
				MTL_ENABLE_DEBUG_INFO = NO;
				SDKROOT = macosx;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
			};
			name = Profile;
		};
		338D0CEA231458BD00FA5F75 /* Profile */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 33E5194F232828860026EE4D /* AppInfo.xcconfig */;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CLANG_ENABLE_MODULES = YES;
				CODE_SIGN_ENTITLEMENTS = Runner/DebugProfile.entitlements;
				CODE_SIGN_STYLE = Automatic;
				COMBINE_HIDPI_IMAGES = YES;
				INFOPLIST_FILE = Runner/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
				);
				PROVISIONING_PROFILE_SPECIFIER = "";
				SWIFT_VERSION = 5.0;
			};
			name = Profile;
		};
		338D0CEB231458BD00FA5F75 /* Profile */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CODE_SIGN_STYLE = Manual;
				PRODUCT_NAME = "$(TARGET_NAME)";
			};
			name = Profile;
		};
		33CC10F92044A3C60003C045 /* Debug */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 9740EEB21CF90195004384FC /* Debug.xcconfig */;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CODE_SIGN_IDENTITY = "-";
				COPY_PHASE_STRIP = NO;
				DEAD_CODE_STRIPPING = YES;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = NO;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				MACOSX_DEPLOYMENT_TARGET = 10.14;
				MTL_ENABLE_DEBUG_INFO = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = macosx;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		33CC10FA2044A3C60003C045 /* Release */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 7AFA3C8E1D35360C0083082E /* Release.xcconfig */;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CODE_SIGN_IDENTITY = "-";
				COPY_PHASE_STRIP = NO;
				DEAD_CODE_STRIPPING = YES;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = NO;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				MACOSX_DEPLOYMENT_TARGET = 10.14;
				MTL_ENABLE_DEBUG_INFO = NO;
				SDKROOT = macosx;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
			};
			name = Release;
		};
		33CC10FC2044A3C60003C045 /* Debug */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 33E5194F232828860026EE4D /* AppInfo.xcconfig */;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CLANG_ENABLE_MODULES = YES;
				CODE_SIGN_ENTITLEMENTS = Runner/DebugProfile.entitlements;
				CODE_SIGN_STYLE = Automatic;
				COMBINE_HIDPI_IMAGES = YES;
				INFOPLIST_FILE = Runner/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
				);
				PROVISIONING_PROFILE_SPECIFIER = "";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				SWIFT_VERSION = 5.0;
			};
			name = Debug;
		};
		33CC10FD2044A3C60003C045 /* Release */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 33E5194F232828860026EE4D /* AppInfo.xcconfig */;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CLANG_ENABLE_MODULES = YES;
				CODE_SIGN_ENTITLEMENTS = Runner/Release.entitlements;
				CODE_SIGN_STYLE = Automatic;
				COMBINE_HIDPI_IMAGES = YES;
				INFOPLIST_FILE = Runner/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
				);
				PROVISIONING_PROFILE_SPECIFIER = "";
				SWIFT_VERSION = 5.0;
			};
			name = Release;
		};
		33CC111C2044C6BA0003C045 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CODE_SIGN_STYLE = Manual;
				PRODUCT_NAME = "$(TARGET_NAME)";
			};
			name = Debug;
		};
		33CC111D2044C6BA0003C045 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CODE_SIGN_STYLE = Automatic;
				PRODUCT_NAME = "$(TARGET_NAME)";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		331C80DE294CF71000263BE5 /* Build configuration list for PBXNativeTarget "RunnerTests" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				331C80DB294CF71000263BE5 /* Debug */,
				331C80DC294CF71000263BE5 /* Release */,
				331C80DD294CF71000263BE5 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		33CC10E82044A3C60003C045 /* Build configuration list for PBXProject "Runner" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				33CC10F92044A3C60003C045 /* Debug */,
				33CC10FA2044A3C60003C045 /* Release */,
				338D0CE9231458BD00FA5F75 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		33CC10FB2044A3C60003C045 /* Build configuration list for PBXNativeTarget "Runner" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				33CC10FC2044A3C60003C045 /* Debug */,
				33CC10FD2044A3C60003C045 /* Release */,
				338D0CEA231458BD00FA5F75 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		33CC111B2044C6BA0003C045 /* Build configuration list for PBXAggregateTarget "Flutter Assemble" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				33CC111C2044C6BA0003C045 /* Debug */,
				33CC111D2044C6BA0003C045 /* Release */,
				338D0CEB231458BD00FA5F75 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 33CC10E52044A3C60003C045 /* Project object */;
}

```

### `frontend/macos/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme`
`size: 3691 bytes`

```xcscheme
<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "1510"
   version = "1.3">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "33CC10EC2044A3C60003C045"
               BuildableName = "frontend.app"
               BlueprintName = "Runner"
               ReferencedContainer = "container:Runner.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      shouldUseLaunchSchemeArgsEnv = "YES">
      <MacroExpansion>
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "33CC10EC2044A3C60003C045"
            BuildableName = "frontend.app"
            BlueprintName = "Runner"
            ReferencedContainer = "container:Runner.xcodeproj">
         </BuildableReference>
      </MacroExpansion>
      <Testables>
         <TestableReference
            skipped = "NO"
            parallelizable = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "331C80D4294CF70F00263BE5"
               BuildableName = "RunnerTests.xctest"
               BlueprintName = "RunnerTests"
               ReferencedContainer = "container:Runner.xcodeproj">
            </BuildableReference>
         </TestableReference>
      </Testables>
   </TestAction>
   <LaunchAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      enableGPUValidationMode = "1"
      allowLocationSimulation = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "33CC10EC2044A3C60003C045"
            BuildableName = "frontend.app"
            BlueprintName = "Runner"
            ReferencedContainer = "container:Runner.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </LaunchAction>
   <ProfileAction
      buildConfiguration = "Profile"
      shouldUseLaunchSchemeArgsEnv = "YES"
      savedToolIdentifier = ""
      useCustomWorkingDirectory = "NO"
      debugDocumentVersioning = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "33CC10EC2044A3C60003C045"
            BuildableName = "frontend.app"
            BlueprintName = "Runner"
            ReferencedContainer = "container:Runner.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction
      buildConfiguration = "Debug">
   </AnalyzeAction>
   <ArchiveAction
      buildConfiguration = "Release"
      revealArchiveInOrganizer = "YES">
   </ArchiveAction>
</Scheme>

```

### `frontend/macos/Runner.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist`
`size: 238 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>IDEDidComputeMac32BitWarning</key>
	<true/>
</dict>
</plist>

```

### `frontend/macos/Runner.xcworkspace/contents.xcworkspacedata`
`size: 152 bytes`

```xcworkspacedata
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "group:Runner.xcodeproj">
   </FileRef>
</Workspace>

```

### `frontend/macos/Runner.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist`
`size: 238 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>IDEDidComputeMac32BitWarning</key>
	<true/>
</dict>
</plist>

```

### `frontend/windows/.gitignore`
`size: 291 bytes`

```
flutter/ephemeral/

# Visual Studio user-specific files.
*.suo
*.user
*.userosscache
*.sln.docstates

# Visual Studio build-related files.
x64/
x86/

# Visual Studio cache files
# files ending in .cache can be ignored
*.[Cc]ache
# but keep track of directories ending in .cache
!*.[Cc]ache/

```

### `frontend/windows/CMakeLists.txt`
`size: 4152 bytes`

```txt
# Project-level configuration.
cmake_minimum_required(VERSION 3.14)
project(frontend LANGUAGES CXX)

# The name of the executable created for the application. Change this to change
# the on-disk name of your application.
set(BINARY_NAME "frontend")

# Explicitly opt in to modern CMake behaviors to avoid warnings with recent
# versions of CMake.
cmake_policy(VERSION 3.14...3.25)

# Define build configuration option.
get_property(IS_MULTICONFIG GLOBAL PROPERTY GENERATOR_IS_MULTI_CONFIG)
if(IS_MULTICONFIG)
  set(CMAKE_CONFIGURATION_TYPES "Debug;Profile;Release"
    CACHE STRING "" FORCE)
else()
  if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE "Debug" CACHE
      STRING "Flutter build mode" FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS
      "Debug" "Profile" "Release")
  endif()
endif()
# Define settings for the Profile build mode.
set(CMAKE_EXE_LINKER_FLAGS_PROFILE "${CMAKE_EXE_LINKER_FLAGS_RELEASE}")
set(CMAKE_SHARED_LINKER_FLAGS_PROFILE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE}")
set(CMAKE_C_FLAGS_PROFILE "${CMAKE_C_FLAGS_RELEASE}")
set(CMAKE_CXX_FLAGS_PROFILE "${CMAKE_CXX_FLAGS_RELEASE}")

# Use Unicode for all projects.
add_definitions(-DUNICODE -D_UNICODE)

# Compilation settings that should be applied to most targets.
#
# Be cautious about adding new options here, as plugins use this function by
# default. In most cases, you should add new options to specific targets instead
# of modifying this function.
function(APPLY_STANDARD_SETTINGS TARGET)
  target_compile_features(${TARGET} PUBLIC cxx_std_17)
  target_compile_options(${TARGET} PRIVATE /W4 /WX /wd"4100")
  target_compile_options(${TARGET} PRIVATE /EHsc)
  target_compile_definitions(${TARGET} PRIVATE "_HAS_EXCEPTIONS=0")
  target_compile_definitions(${TARGET} PRIVATE "$<$<CONFIG:Debug>:_DEBUG>")
endfunction()

# Flutter library and tool build rules.
set(FLUTTER_MANAGED_DIR "${CMAKE_CURRENT_SOURCE_DIR}/flutter")
add_subdirectory(${FLUTTER_MANAGED_DIR})

# Application build; see runner/CMakeLists.txt.
add_subdirectory("runner")


# Generated plugin build rules, which manage building the plugins and adding
# them to the application.
include(flutter/generated_plugins.cmake)


# === Installation ===
# Support files are copied into place next to the executable, so that it can
# run in place. This is done instead of making a separate bundle (as on Linux)
# so that building and running from within Visual Studio will work.
set(BUILD_BUNDLE_DIR "$<TARGET_FILE_DIR:${BINARY_NAME}>")
# Make the "install" step default, as it's required to run.
set(CMAKE_VS_INCLUDE_INSTALL_TO_DEFAULT_BUILD 1)
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX "${BUILD_BUNDLE_DIR}" CACHE PATH "..." FORCE)
endif()

set(INSTALL_BUNDLE_DATA_DIR "${CMAKE_INSTALL_PREFIX}/data")
set(INSTALL_BUNDLE_LIB_DIR "${CMAKE_INSTALL_PREFIX}")

install(TARGETS ${BINARY_NAME} RUNTIME DESTINATION "${CMAKE_INSTALL_PREFIX}"
  COMPONENT Runtime)

install(FILES "${FLUTTER_ICU_DATA_FILE}" DESTINATION "${INSTALL_BUNDLE_DATA_DIR}"
  COMPONENT Runtime)

install(FILES "${FLUTTER_LIBRARY}" DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
  COMPONENT Runtime)

if(PLUGIN_BUNDLED_LIBRARIES)
  install(FILES "${PLUGIN_BUNDLED_LIBRARIES}"
    DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
    COMPONENT Runtime)
endif()

# Copy the native assets provided by the build.dart from all packages.
set(NATIVE_ASSETS_DIR "${PROJECT_BUILD_DIR}native_assets/windows/")
install(DIRECTORY "${NATIVE_ASSETS_DIR}"
   DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
   COMPONENT Runtime)

# Fully re-copy the assets directory on each build to avoid having stale files
# from a previous install.
set(FLUTTER_ASSET_DIR_NAME "flutter_assets")
install(CODE "
  file(REMOVE_RECURSE \"${INSTALL_BUNDLE_DATA_DIR}/${FLUTTER_ASSET_DIR_NAME}\")
  " COMPONENT Runtime)
install(DIRECTORY "${PROJECT_BUILD_DIR}/${FLUTTER_ASSET_DIR_NAME}"
  DESTINATION "${INSTALL_BUNDLE_DATA_DIR}" COMPONENT Runtime)

# Install the AOT library on non-Debug builds only.
install(FILES "${AOT_LIBRARY}" DESTINATION "${INSTALL_BUNDLE_DATA_DIR}"
  CONFIGURATIONS Profile;Release
  COMPONENT Runtime)

```

### `frontend/windows/runner/CMakeLists.txt`
`size: 1796 bytes`

```txt
cmake_minimum_required(VERSION 3.14)
project(runner LANGUAGES CXX)

# Define the application target. To change its name, change BINARY_NAME in the
# top-level CMakeLists.txt, not the value here, or `flutter run` will no longer
# work.
#
# Any new source files that you add to the application should be added here.
add_executable(${BINARY_NAME} WIN32
  "flutter_window.cpp"
  "main.cpp"
  "utils.cpp"
  "win32_window.cpp"
  "${FLUTTER_MANAGED_DIR}/generated_plugin_registrant.cc"
  "Runner.rc"
  "runner.exe.manifest"
)

# Apply the standard set of build settings. This can be removed for applications
# that need different build settings.
apply_standard_settings(${BINARY_NAME})

# Add preprocessor definitions for the build version.
target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION=\"${FLUTTER_VERSION}\"")
target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_MAJOR=${FLUTTER_VERSION_MAJOR}")
target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_MINOR=${FLUTTER_VERSION_MINOR}")
target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_PATCH=${FLUTTER_VERSION_PATCH}")
target_compile_definitions(${BINARY_NAME} PRIVATE "FLUTTER_VERSION_BUILD=${FLUTTER_VERSION_BUILD}")

# Disable Windows macros that collide with C++ standard library functions.
target_compile_definitions(${BINARY_NAME} PRIVATE "NOMINMAX")

# Add dependency libraries and include directories. Add any application-specific
# dependencies here.
target_link_libraries(${BINARY_NAME} PRIVATE flutter flutter_wrapper_app)
target_link_libraries(${BINARY_NAME} PRIVATE "dwmapi.lib")
target_include_directories(${BINARY_NAME} PRIVATE "${CMAKE_SOURCE_DIR}")

# Run the Flutter tool portions of the build. This must not be removed.
add_dependencies(${BINARY_NAME} flutter_assemble)

```

### `frontend/windows/runner/Runner.rc`
`size: 3029 bytes`

```rc
// Microsoft Visual C++ generated resource script.
//
#pragma code_page(65001)
#include "resource.h"

#define APSTUDIO_READONLY_SYMBOLS
/////////////////////////////////////////////////////////////////////////////
//
// Generated from the TEXTINCLUDE 2 resource.
//
#include "winres.h"

/////////////////////////////////////////////////////////////////////////////
#undef APSTUDIO_READONLY_SYMBOLS

/////////////////////////////////////////////////////////////////////////////
// English (United States) resources

#if !defined(AFX_RESOURCE_DLL) || defined(AFX_TARG_ENU)
LANGUAGE LANG_ENGLISH, SUBLANG_ENGLISH_US

#ifdef APSTUDIO_INVOKED
/////////////////////////////////////////////////////////////////////////////
//
// TEXTINCLUDE
//

1 TEXTINCLUDE
BEGIN
    "resource.h\0"
END

2 TEXTINCLUDE
BEGIN
    "#include ""winres.h""\r\n"
    "\0"
END

3 TEXTINCLUDE
BEGIN
    "\r\n"
    "\0"
END

#endif    // APSTUDIO_INVOKED


/////////////////////////////////////////////////////////////////////////////
//
// Icon
//

// Icon with lowest ID value placed first to ensure application icon
// remains consistent on all systems.
IDI_APP_ICON            ICON                    "resources\\app_icon.ico"


/////////////////////////////////////////////////////////////////////////////
//
// Version
//

#if defined(FLUTTER_VERSION_MAJOR) && defined(FLUTTER_VERSION_MINOR) && defined(FLUTTER_VERSION_PATCH) && defined(FLUTTER_VERSION_BUILD)
#define VERSION_AS_NUMBER FLUTTER_VERSION_MAJOR,FLUTTER_VERSION_MINOR,FLUTTER_VERSION_PATCH,FLUTTER_VERSION_BUILD
#else
#define VERSION_AS_NUMBER 1,0,0,0
#endif

#if defined(FLUTTER_VERSION)
#define VERSION_AS_STRING FLUTTER_VERSION
#else
#define VERSION_AS_STRING "1.0.0"
#endif

VS_VERSION_INFO VERSIONINFO
 FILEVERSION VERSION_AS_NUMBER
 PRODUCTVERSION VERSION_AS_NUMBER
 FILEFLAGSMASK VS_FFI_FILEFLAGSMASK
#ifdef _DEBUG
 FILEFLAGS VS_FF_DEBUG
#else
 FILEFLAGS 0x0L
#endif
 FILEOS VOS__WINDOWS32
 FILETYPE VFT_APP
 FILESUBTYPE 0x0L
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904e4"
        BEGIN
            VALUE "CompanyName", "com.example" "\0"
            VALUE "FileDescription", "frontend" "\0"
            VALUE "FileVersion", VERSION_AS_STRING "\0"
            VALUE "InternalName", "frontend" "\0"
            VALUE "LegalCopyright", "Copyright (C) 2025 com.example. All rights reserved." "\0"
            VALUE "OriginalFilename", "frontend.exe" "\0"
            VALUE "ProductName", "frontend" "\0"
            VALUE "ProductVersion", VERSION_AS_STRING "\0"
        END
    END
    BLOCK "VarFileInfo"
    BEGIN
        VALUE "Translation", 0x409, 1252
    END
END

#endif    // English (United States) resources
/////////////////////////////////////////////////////////////////////////////



#ifndef APSTUDIO_INVOKED
/////////////////////////////////////////////////////////////////////////////
//
// Generated from the TEXTINCLUDE 3 resource.
//


/////////////////////////////////////////////////////////////////////////////
#endif    // not APSTUDIO_INVOKED

```

### `frontend/windows/runner/flutter_window.cpp`
`size: 2122 bytes`

```cpp
#include "flutter_window.h"

#include <optional>

#include "flutter/generated_plugin_registrant.h"

FlutterWindow::FlutterWindow(const flutter::DartProject& project)
    : project_(project) {}

FlutterWindow::~FlutterWindow() {}

bool FlutterWindow::OnCreate() {
  if (!Win32Window::OnCreate()) {
    return false;
  }

  RECT frame = GetClientArea();

  // The size here must match the window dimensions to avoid unnecessary surface
  // creation / destruction in the startup path.
  flutter_controller_ = std::make_unique<flutter::FlutterViewController>(
      frame.right - frame.left, frame.bottom - frame.top, project_);
  // Ensure that basic setup of the controller was successful.
  if (!flutter_controller_->engine() || !flutter_controller_->view()) {
    return false;
  }
  RegisterPlugins(flutter_controller_->engine());
  SetChildContent(flutter_controller_->view()->GetNativeWindow());

  flutter_controller_->engine()->SetNextFrameCallback([&]() {
    this->Show();
  });

  // Flutter can complete the first frame before the "show window" callback is
  // registered. The following call ensures a frame is pending to ensure the
  // window is shown. It is a no-op if the first frame hasn't completed yet.
  flutter_controller_->ForceRedraw();

  return true;
}

void FlutterWindow::OnDestroy() {
  if (flutter_controller_) {
    flutter_controller_ = nullptr;
  }

  Win32Window::OnDestroy();
}

LRESULT
FlutterWindow::MessageHandler(HWND hwnd, UINT const message,
                              WPARAM const wparam,
                              LPARAM const lparam) noexcept {
  // Give Flutter, including plugins, an opportunity to handle window messages.
  if (flutter_controller_) {
    std::optional<LRESULT> result =
        flutter_controller_->HandleTopLevelWindowProc(hwnd, message, wparam,
                                                      lparam);
    if (result) {
      return *result;
    }
  }

  switch (message) {
    case WM_FONTCHANGE:
      flutter_controller_->engine()->ReloadSystemFonts();
      break;
  }

  return Win32Window::MessageHandler(hwnd, message, wparam, lparam);
}

```

### `frontend/windows/runner/flutter_window.h`
`size: 928 bytes`

```h
#ifndef RUNNER_FLUTTER_WINDOW_H_
#define RUNNER_FLUTTER_WINDOW_H_

#include <flutter/dart_project.h>
#include <flutter/flutter_view_controller.h>

#include <memory>

#include "win32_window.h"

// A window that does nothing but host a Flutter view.
class FlutterWindow : public Win32Window {
 public:
  // Creates a new FlutterWindow hosting a Flutter view running |project|.
  explicit FlutterWindow(const flutter::DartProject& project);
  virtual ~FlutterWindow();

 protected:
  // Win32Window:
  bool OnCreate() override;
  void OnDestroy() override;
  LRESULT MessageHandler(HWND window, UINT const message, WPARAM const wparam,
                         LPARAM const lparam) noexcept override;

 private:
  // The project to run.
  flutter::DartProject project_;

  // The Flutter instance hosted by this window.
  std::unique_ptr<flutter::FlutterViewController> flutter_controller_;
};

#endif  // RUNNER_FLUTTER_WINDOW_H_

```

### `frontend/windows/runner/main.cpp`
`size: 1261 bytes`

```cpp
#include <flutter/dart_project.h>
#include <flutter/flutter_view_controller.h>
#include <windows.h>

#include "flutter_window.h"
#include "utils.h"

int APIENTRY wWinMain(_In_ HINSTANCE instance, _In_opt_ HINSTANCE prev,
                      _In_ wchar_t *command_line, _In_ int show_command) {
  // Attach to console when present (e.g., 'flutter run') or create a
  // new console when running with a debugger.
  if (!::AttachConsole(ATTACH_PARENT_PROCESS) && ::IsDebuggerPresent()) {
    CreateAndAttachConsole();
  }

  // Initialize COM, so that it is available for use in the library and/or
  // plugins.
  ::CoInitializeEx(nullptr, COINIT_APARTMENTTHREADED);

  flutter::DartProject project(L"data");

  std::vector<std::string> command_line_arguments =
      GetCommandLineArguments();

  project.set_dart_entrypoint_arguments(std::move(command_line_arguments));

  FlutterWindow window(project);
  Win32Window::Point origin(10, 10);
  Win32Window::Size size(1280, 720);
  if (!window.Create(L"frontend", origin, size)) {
    return EXIT_FAILURE;
  }
  window.SetQuitOnClose(true);

  ::MSG msg;
  while (::GetMessage(&msg, nullptr, 0, 0)) {
    ::TranslateMessage(&msg);
    ::DispatchMessage(&msg);
  }

  ::CoUninitialize();
  return EXIT_SUCCESS;
}

```

### `frontend/windows/runner/resource.h`
`size: 432 bytes`

```h
//{{NO_DEPENDENCIES}}
// Microsoft Visual C++ generated include file.
// Used by Runner.rc
//
#define IDI_APP_ICON                    101

// Next default values for new objects
//
#ifdef APSTUDIO_INVOKED
#ifndef APSTUDIO_READONLY_SYMBOLS
#define _APS_NEXT_RESOURCE_VALUE        102
#define _APS_NEXT_COMMAND_VALUE         40001
#define _APS_NEXT_CONTROL_VALUE         1001
#define _APS_NEXT_SYMED_VALUE           101
#endif
#endif

```

### `frontend/windows/runner/runner.exe.manifest`
`size: 602 bytes`

```manifest
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <application xmlns="urn:schemas-microsoft-com:asm.v3">
    <windowsSettings>
      <dpiAwareness xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">PerMonitorV2</dpiAwareness>
    </windowsSettings>
  </application>
  <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">
    <application>
      <!-- Windows 10 and Windows 11 -->
      <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/>
    </application>
  </compatibility>
</assembly>

```

### `frontend/windows/runner/utils.cpp`
`size: 1797 bytes`

```cpp
#include "utils.h"

#include <flutter_windows.h>
#include <io.h>
#include <stdio.h>
#include <windows.h>

#include <iostream>

void CreateAndAttachConsole() {
  if (::AllocConsole()) {
    FILE *unused;
    if (freopen_s(&unused, "CONOUT$", "w", stdout)) {
      _dup2(_fileno(stdout), 1);
    }
    if (freopen_s(&unused, "CONOUT$", "w", stderr)) {
      _dup2(_fileno(stdout), 2);
    }
    std::ios::sync_with_stdio();
    FlutterDesktopResyncOutputStreams();
  }
}

std::vector<std::string> GetCommandLineArguments() {
  // Convert the UTF-16 command line arguments to UTF-8 for the Engine to use.
  int argc;
  wchar_t** argv = ::CommandLineToArgvW(::GetCommandLineW(), &argc);
  if (argv == nullptr) {
    return std::vector<std::string>();
  }

  std::vector<std::string> command_line_arguments;

  // Skip the first argument as it's the binary name.
  for (int i = 1; i < argc; i++) {
    command_line_arguments.push_back(Utf8FromUtf16(argv[i]));
  }

  ::LocalFree(argv);

  return command_line_arguments;
}

std::string Utf8FromUtf16(const wchar_t* utf16_string) {
  if (utf16_string == nullptr) {
    return std::string();
  }
  unsigned int target_length = ::WideCharToMultiByte(
      CP_UTF8, WC_ERR_INVALID_CHARS, utf16_string,
      -1, nullptr, 0, nullptr, nullptr)
    -1; // remove the trailing null character
  int input_length = (int)wcslen(utf16_string);
  std::string utf8_string;
  if (target_length == 0 || target_length > utf8_string.max_size()) {
    return utf8_string;
  }
  utf8_string.resize(target_length);
  int converted_length = ::WideCharToMultiByte(
      CP_UTF8, WC_ERR_INVALID_CHARS, utf16_string,
      input_length, utf8_string.data(), target_length, nullptr, nullptr);
  if (converted_length == 0) {
    return std::string();
  }
  return utf8_string;
}

```

### `frontend/windows/runner/utils.h`
`size: 672 bytes`

```h
#ifndef RUNNER_UTILS_H_
#define RUNNER_UTILS_H_

#include <string>
#include <vector>

// Creates a console for the process, and redirects stdout and stderr to
// it for both the runner and the Flutter library.
void CreateAndAttachConsole();

// Takes a null-terminated wchar_t* encoded in UTF-16 and returns a std::string
// encoded in UTF-8. Returns an empty std::string on failure.
std::string Utf8FromUtf16(const wchar_t* utf16_string);

// Gets the command line arguments passed in as a std::vector<std::string>,
// encoded in UTF-8. Returns an empty std::vector<std::string> on failure.
std::vector<std::string> GetCommandLineArguments();

#endif  // RUNNER_UTILS_H_

```

### `frontend/windows/runner/win32_window.cpp`
`size: 8534 bytes`

```cpp
#include "win32_window.h"

#include <dwmapi.h>
#include <flutter_windows.h>

#include "resource.h"

namespace {

/// Window attribute that enables dark mode window decorations.
///
/// Redefined in case the developer's machine has a Windows SDK older than
/// version 10.0.22000.0.
/// See: https://docs.microsoft.com/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
#ifndef DWMWA_USE_IMMERSIVE_DARK_MODE
#define DWMWA_USE_IMMERSIVE_DARK_MODE 20
#endif

constexpr const wchar_t kWindowClassName[] = L"FLUTTER_RUNNER_WIN32_WINDOW";

/// Registry key for app theme preference.
///
/// A value of 0 indicates apps should use dark mode. A non-zero or missing
/// value indicates apps should use light mode.
constexpr const wchar_t kGetPreferredBrightnessRegKey[] =
  L"Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize";
constexpr const wchar_t kGetPreferredBrightnessRegValue[] = L"AppsUseLightTheme";

// The number of Win32Window objects that currently exist.
static int g_active_window_count = 0;

using EnableNonClientDpiScaling = BOOL __stdcall(HWND hwnd);

// Scale helper to convert logical scaler values to physical using passed in
// scale factor
int Scale(int source, double scale_factor) {
  return static_cast<int>(source * scale_factor);
}

// Dynamically loads the |EnableNonClientDpiScaling| from the User32 module.
// This API is only needed for PerMonitor V1 awareness mode.
void EnableFullDpiSupportIfAvailable(HWND hwnd) {
  HMODULE user32_module = LoadLibraryA("User32.dll");
  if (!user32_module) {
    return;
  }
  auto enable_non_client_dpi_scaling =
      reinterpret_cast<EnableNonClientDpiScaling*>(
          GetProcAddress(user32_module, "EnableNonClientDpiScaling"));
  if (enable_non_client_dpi_scaling != nullptr) {
    enable_non_client_dpi_scaling(hwnd);
  }
  FreeLibrary(user32_module);
}

}  // namespace

// Manages the Win32Window's window class registration.
class WindowClassRegistrar {
 public:
  ~WindowClassRegistrar() = default;

  // Returns the singleton registrar instance.
  static WindowClassRegistrar* GetInstance() {
    if (!instance_) {
      instance_ = new WindowClassRegistrar();
    }
    return instance_;
  }

  // Returns the name of the window class, registering the class if it hasn't
  // previously been registered.
  const wchar_t* GetWindowClass();

  // Unregisters the window class. Should only be called if there are no
  // instances of the window.
  void UnregisterWindowClass();

 private:
  WindowClassRegistrar() = default;

  static WindowClassRegistrar* instance_;

  bool class_registered_ = false;
};

WindowClassRegistrar* WindowClassRegistrar::instance_ = nullptr;

const wchar_t* WindowClassRegistrar::GetWindowClass() {
  if (!class_registered_) {
    WNDCLASS window_class{};
    window_class.hCursor = LoadCursor(nullptr, IDC_ARROW);
    window_class.lpszClassName = kWindowClassName;
    window_class.style = CS_HREDRAW | CS_VREDRAW;
    window_class.cbClsExtra = 0;
    window_class.cbWndExtra = 0;
    window_class.hInstance = GetModuleHandle(nullptr);
    window_class.hIcon =
        LoadIcon(window_class.hInstance, MAKEINTRESOURCE(IDI_APP_ICON));
    window_class.hbrBackground = 0;
    window_class.lpszMenuName = nullptr;
    window_class.lpfnWndProc = Win32Window::WndProc;
    RegisterClass(&window_class);
    class_registered_ = true;
  }
  return kWindowClassName;
}

void WindowClassRegistrar::UnregisterWindowClass() {
  UnregisterClass(kWindowClassName, nullptr);
  class_registered_ = false;
}

Win32Window::Win32Window() {
  ++g_active_window_count;
}

Win32Window::~Win32Window() {
  --g_active_window_count;
  Destroy();
}

bool Win32Window::Create(const std::wstring& title,
                         const Point& origin,
                         const Size& size) {
  Destroy();

  const wchar_t* window_class =
      WindowClassRegistrar::GetInstance()->GetWindowClass();

  const POINT target_point = {static_cast<LONG>(origin.x),
                              static_cast<LONG>(origin.y)};
  HMONITOR monitor = MonitorFromPoint(target_point, MONITOR_DEFAULTTONEAREST);
  UINT dpi = FlutterDesktopGetDpiForMonitor(monitor);
  double scale_factor = dpi / 96.0;

  HWND window = CreateWindow(
      window_class, title.c_str(), WS_OVERLAPPEDWINDOW,
      Scale(origin.x, scale_factor), Scale(origin.y, scale_factor),
      Scale(size.width, scale_factor), Scale(size.height, scale_factor),
      nullptr, nullptr, GetModuleHandle(nullptr), this);

  if (!window) {
    return false;
  }

  UpdateTheme(window);

  return OnCreate();
}

bool Win32Window::Show() {
  return ShowWindow(window_handle_, SW_SHOWNORMAL);
}

// static
LRESULT CALLBACK Win32Window::WndProc(HWND const window,
                                      UINT const message,
                                      WPARAM const wparam,
                                      LPARAM const lparam) noexcept {
  if (message == WM_NCCREATE) {
    auto window_struct = reinterpret_cast<CREATESTRUCT*>(lparam);
    SetWindowLongPtr(window, GWLP_USERDATA,
                     reinterpret_cast<LONG_PTR>(window_struct->lpCreateParams));

    auto that = static_cast<Win32Window*>(window_struct->lpCreateParams);
    EnableFullDpiSupportIfAvailable(window);
    that->window_handle_ = window;
  } else if (Win32Window* that = GetThisFromHandle(window)) {
    return that->MessageHandler(window, message, wparam, lparam);
  }

  return DefWindowProc(window, message, wparam, lparam);
}

LRESULT
Win32Window::MessageHandler(HWND hwnd,
                            UINT const message,
                            WPARAM const wparam,
                            LPARAM const lparam) noexcept {
  switch (message) {
    case WM_DESTROY:
      window_handle_ = nullptr;
      Destroy();
      if (quit_on_close_) {
        PostQuitMessage(0);
      }
      return 0;

    case WM_DPICHANGED: {
      auto newRectSize = reinterpret_cast<RECT*>(lparam);
      LONG newWidth = newRectSize->right - newRectSize->left;
      LONG newHeight = newRectSize->bottom - newRectSize->top;

      SetWindowPos(hwnd, nullptr, newRectSize->left, newRectSize->top, newWidth,
                   newHeight, SWP_NOZORDER | SWP_NOACTIVATE);

      return 0;
    }
    case WM_SIZE: {
      RECT rect = GetClientArea();
      if (child_content_ != nullptr) {
        // Size and position the child window.
        MoveWindow(child_content_, rect.left, rect.top, rect.right - rect.left,
                   rect.bottom - rect.top, TRUE);
      }
      return 0;
    }

    case WM_ACTIVATE:
      if (child_content_ != nullptr) {
        SetFocus(child_content_);
      }
      return 0;

    case WM_DWMCOLORIZATIONCOLORCHANGED:
      UpdateTheme(hwnd);
      return 0;
  }

  return DefWindowProc(window_handle_, message, wparam, lparam);
}

void Win32Window::Destroy() {
  OnDestroy();

  if (window_handle_) {
    DestroyWindow(window_handle_);
    window_handle_ = nullptr;
  }
  if (g_active_window_count == 0) {
    WindowClassRegistrar::GetInstance()->UnregisterWindowClass();
  }
}

Win32Window* Win32Window::GetThisFromHandle(HWND const window) noexcept {
  return reinterpret_cast<Win32Window*>(
      GetWindowLongPtr(window, GWLP_USERDATA));
}

void Win32Window::SetChildContent(HWND content) {
  child_content_ = content;
  SetParent(content, window_handle_);
  RECT frame = GetClientArea();

  MoveWindow(content, frame.left, frame.top, frame.right - frame.left,
             frame.bottom - frame.top, true);

  SetFocus(child_content_);
}

RECT Win32Window::GetClientArea() {
  RECT frame;
  GetClientRect(window_handle_, &frame);
  return frame;
}

HWND Win32Window::GetHandle() {
  return window_handle_;
}

void Win32Window::SetQuitOnClose(bool quit_on_close) {
  quit_on_close_ = quit_on_close;
}

bool Win32Window::OnCreate() {
  // No-op; provided for subclasses.
  return true;
}

void Win32Window::OnDestroy() {
  // No-op; provided for subclasses.
}

void Win32Window::UpdateTheme(HWND const window) {
  DWORD light_mode;
  DWORD light_mode_size = sizeof(light_mode);
  LSTATUS result = RegGetValue(HKEY_CURRENT_USER, kGetPreferredBrightnessRegKey,
                               kGetPreferredBrightnessRegValue,
                               RRF_RT_REG_DWORD, nullptr, &light_mode,
                               &light_mode_size);

  if (result == ERROR_SUCCESS) {
    BOOL enable_dark_mode = light_mode == 0;
    DwmSetWindowAttribute(window, DWMWA_USE_IMMERSIVE_DARK_MODE,
                          &enable_dark_mode, sizeof(enable_dark_mode));
  }
}

```

### `frontend/windows/runner/win32_window.h`
`size: 3522 bytes`

```h
#ifndef RUNNER_WIN32_WINDOW_H_
#define RUNNER_WIN32_WINDOW_H_

#include <windows.h>

#include <functional>
#include <memory>
#include <string>

// A class abstraction for a high DPI-aware Win32 Window. Intended to be
// inherited from by classes that wish to specialize with custom
// rendering and input handling
class Win32Window {
 public:
  struct Point {
    unsigned int x;
    unsigned int y;
    Point(unsigned int x, unsigned int y) : x(x), y(y) {}
  };

  struct Size {
    unsigned int width;
    unsigned int height;
    Size(unsigned int width, unsigned int height)
        : width(width), height(height) {}
  };

  Win32Window();
  virtual ~Win32Window();

  // Creates a win32 window with |title| that is positioned and sized using
  // |origin| and |size|. New windows are created on the default monitor. Window
  // sizes are specified to the OS in physical pixels, hence to ensure a
  // consistent size this function will scale the inputted width and height as
  // as appropriate for the default monitor. The window is invisible until
  // |Show| is called. Returns true if the window was created successfully.
  bool Create(const std::wstring& title, const Point& origin, const Size& size);

  // Show the current window. Returns true if the window was successfully shown.
  bool Show();

  // Release OS resources associated with window.
  void Destroy();

  // Inserts |content| into the window tree.
  void SetChildContent(HWND content);

  // Returns the backing Window handle to enable clients to set icon and other
  // window properties. Returns nullptr if the window has been destroyed.
  HWND GetHandle();

  // If true, closing this window will quit the application.
  void SetQuitOnClose(bool quit_on_close);

  // Return a RECT representing the bounds of the current client area.
  RECT GetClientArea();

 protected:
  // Processes and route salient window messages for mouse handling,
  // size change and DPI. Delegates handling of these to member overloads that
  // inheriting classes can handle.
  virtual LRESULT MessageHandler(HWND window,
                                 UINT const message,
                                 WPARAM const wparam,
                                 LPARAM const lparam) noexcept;

  // Called when CreateAndShow is called, allowing subclass window-related
  // setup. Subclasses should return false if setup fails.
  virtual bool OnCreate();

  // Called when Destroy is called.
  virtual void OnDestroy();

 private:
  friend class WindowClassRegistrar;

  // OS callback called by message pump. Handles the WM_NCCREATE message which
  // is passed when the non-client area is being created and enables automatic
  // non-client DPI scaling so that the non-client area automatically
  // responds to changes in DPI. All other messages are handled by
  // MessageHandler.
  static LRESULT CALLBACK WndProc(HWND const window,
                                  UINT const message,
                                  WPARAM const wparam,
                                  LPARAM const lparam) noexcept;

  // Retrieves a class instance pointer for |window|
  static Win32Window* GetThisFromHandle(HWND const window) noexcept;

  // Update the window frame's theme to match the system theme.
  static void UpdateTheme(HWND const window);

  bool quit_on_close_ = false;

  // window handle for top level window.
  HWND window_handle_ = nullptr;

  // window handle for hosted content.
  HWND child_content_ = nullptr;
};

#endif  // RUNNER_WIN32_WINDOW_H_

```

### `frontend/windows/flutter/CMakeLists.txt`
`size: 3742 bytes`

```txt
# This file controls Flutter-level build steps. It should not be edited.
cmake_minimum_required(VERSION 3.14)

set(EPHEMERAL_DIR "${CMAKE_CURRENT_SOURCE_DIR}/ephemeral")

# Configuration provided via flutter tool.
include(${EPHEMERAL_DIR}/generated_config.cmake)

# TODO: Move the rest of this into files in ephemeral. See
# https://github.com/flutter/flutter/issues/57146.
set(WRAPPER_ROOT "${EPHEMERAL_DIR}/cpp_client_wrapper")

# Set fallback configurations for older versions of the flutter tool.
if (NOT DEFINED FLUTTER_TARGET_PLATFORM)
  set(FLUTTER_TARGET_PLATFORM "windows-x64")
endif()

# === Flutter Library ===
set(FLUTTER_LIBRARY "${EPHEMERAL_DIR}/flutter_windows.dll")

# Published to parent scope for install step.
set(FLUTTER_LIBRARY ${FLUTTER_LIBRARY} PARENT_SCOPE)
set(FLUTTER_ICU_DATA_FILE "${EPHEMERAL_DIR}/icudtl.dat" PARENT_SCOPE)
set(PROJECT_BUILD_DIR "${PROJECT_DIR}/build/" PARENT_SCOPE)
set(AOT_LIBRARY "${PROJECT_DIR}/build/windows/app.so" PARENT_SCOPE)

list(APPEND FLUTTER_LIBRARY_HEADERS
  "flutter_export.h"
  "flutter_windows.h"
  "flutter_messenger.h"
  "flutter_plugin_registrar.h"
  "flutter_texture_registrar.h"
)
list(TRANSFORM FLUTTER_LIBRARY_HEADERS PREPEND "${EPHEMERAL_DIR}/")
add_library(flutter INTERFACE)
target_include_directories(flutter INTERFACE
  "${EPHEMERAL_DIR}"
)
target_link_libraries(flutter INTERFACE "${FLUTTER_LIBRARY}.lib")
add_dependencies(flutter flutter_assemble)

# === Wrapper ===
list(APPEND CPP_WRAPPER_SOURCES_CORE
  "core_implementations.cc"
  "standard_codec.cc"
)
list(TRANSFORM CPP_WRAPPER_SOURCES_CORE PREPEND "${WRAPPER_ROOT}/")
list(APPEND CPP_WRAPPER_SOURCES_PLUGIN
  "plugin_registrar.cc"
)
list(TRANSFORM CPP_WRAPPER_SOURCES_PLUGIN PREPEND "${WRAPPER_ROOT}/")
list(APPEND CPP_WRAPPER_SOURCES_APP
  "flutter_engine.cc"
  "flutter_view_controller.cc"
)
list(TRANSFORM CPP_WRAPPER_SOURCES_APP PREPEND "${WRAPPER_ROOT}/")

# Wrapper sources needed for a plugin.
add_library(flutter_wrapper_plugin STATIC
  ${CPP_WRAPPER_SOURCES_CORE}
  ${CPP_WRAPPER_SOURCES_PLUGIN}
)
apply_standard_settings(flutter_wrapper_plugin)
set_target_properties(flutter_wrapper_plugin PROPERTIES
  POSITION_INDEPENDENT_CODE ON)
set_target_properties(flutter_wrapper_plugin PROPERTIES
  CXX_VISIBILITY_PRESET hidden)
target_link_libraries(flutter_wrapper_plugin PUBLIC flutter)
target_include_directories(flutter_wrapper_plugin PUBLIC
  "${WRAPPER_ROOT}/include"
)
add_dependencies(flutter_wrapper_plugin flutter_assemble)

# Wrapper sources needed for the runner.
add_library(flutter_wrapper_app STATIC
  ${CPP_WRAPPER_SOURCES_CORE}
  ${CPP_WRAPPER_SOURCES_APP}
)
apply_standard_settings(flutter_wrapper_app)
target_link_libraries(flutter_wrapper_app PUBLIC flutter)
target_include_directories(flutter_wrapper_app PUBLIC
  "${WRAPPER_ROOT}/include"
)
add_dependencies(flutter_wrapper_app flutter_assemble)

# === Flutter tool backend ===
# _phony_ is a non-existent file to force this command to run every time,
# since currently there's no way to get a full input/output list from the
# flutter tool.
set(PHONY_OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/_phony_")
set_source_files_properties("${PHONY_OUTPUT}" PROPERTIES SYMBOLIC TRUE)
add_custom_command(
  OUTPUT ${FLUTTER_LIBRARY} ${FLUTTER_LIBRARY_HEADERS}
    ${CPP_WRAPPER_SOURCES_CORE} ${CPP_WRAPPER_SOURCES_PLUGIN}
    ${CPP_WRAPPER_SOURCES_APP}
    ${PHONY_OUTPUT}
  COMMAND ${CMAKE_COMMAND} -E env
    ${FLUTTER_TOOL_ENVIRONMENT}
    "${FLUTTER_ROOT}/packages/flutter_tools/bin/tool_backend.bat"
      ${FLUTTER_TARGET_PLATFORM} $<CONFIG>
  VERBATIM
)
add_custom_target(flutter_assemble DEPENDS
  "${FLUTTER_LIBRARY}"
  ${FLUTTER_LIBRARY_HEADERS}
  ${CPP_WRAPPER_SOURCES_CORE}
  ${CPP_WRAPPER_SOURCES_PLUGIN}
  ${CPP_WRAPPER_SOURCES_APP}
)

```

### `frontend/windows/flutter/generated_plugin_registrant.cc`
`size: 164 bytes`

```cc
//
//  Generated file. Do not edit.
//

// clang-format off

#include "generated_plugin_registrant.h"


void RegisterPlugins(flutter::PluginRegistry* registry) {
}

```

### `frontend/windows/flutter/generated_plugin_registrant.h`
`size: 302 bytes`

```h
//
//  Generated file. Do not edit.
//

// clang-format off

#ifndef GENERATED_PLUGIN_REGISTRANT_
#define GENERATED_PLUGIN_REGISTRANT_

#include <flutter/plugin_registry.h>

// Registers Flutter plugins.
void RegisterPlugins(flutter::PluginRegistry* registry);

#endif  // GENERATED_PLUGIN_REGISTRANT_

```

### `frontend/windows/flutter/generated_plugins.cmake`
`size: 743 bytes`

```cmake
#
# Generated file, do not edit.
#

list(APPEND FLUTTER_PLUGIN_LIST
)

list(APPEND FLUTTER_FFI_PLUGIN_LIST
)

set(PLUGIN_BUNDLED_LIBRARIES)

foreach(plugin ${FLUTTER_PLUGIN_LIST})
  add_subdirectory(flutter/ephemeral/.plugin_symlinks/${plugin}/windows plugins/${plugin})
  target_link_libraries(${BINARY_NAME} PRIVATE ${plugin}_plugin)
  list(APPEND PLUGIN_BUNDLED_LIBRARIES $<TARGET_FILE:${plugin}_plugin>)
  list(APPEND PLUGIN_BUNDLED_LIBRARIES ${${plugin}_bundled_libraries})
endforeach(plugin)

foreach(ffi_plugin ${FLUTTER_FFI_PLUGIN_LIST})
  add_subdirectory(flutter/ephemeral/.plugin_symlinks/${ffi_plugin}/windows plugins/${ffi_plugin})
  list(APPEND PLUGIN_BUNDLED_LIBRARIES ${${ffi_plugin}_bundled_libraries})
endforeach(ffi_plugin)

```

### `frontend/android/.gitignore`
`size: 253 bytes`

```
gradle-wrapper.jar
/.gradle
/captures/
/gradlew
/gradlew.bat
/local.properties
GeneratedPluginRegistrant.java
.cxx/

# Remember to never publicly share your keystore.
# See https://flutter.dev/to/reference-keystore
key.properties
**/*.keystore
**/*.jks

```

### `frontend/android/build.gradle.kts`
`size: 515 bytes`

```kts
allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

val newBuildDir: Directory = rootProject.layout.buildDirectory.dir("../../build").get()
rootProject.layout.buildDirectory.value(newBuildDir)

subprojects {
    val newSubprojectBuildDir: Directory = newBuildDir.dir(project.name)
    project.layout.buildDirectory.value(newSubprojectBuildDir)
}
subprojects {
    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}

```

### `frontend/android/gradle.properties`
`size: 166 bytes`

```properties
org.gradle.jvmargs=-Xmx8G -XX:MaxMetaspaceSize=4G -XX:ReservedCodeCacheSize=512m -XX:+HeapDumpOnOutOfMemoryError
android.useAndroidX=true
android.enableJetifier=true

```

### `frontend/android/settings.gradle.kts`
`size: 738 bytes`

```kts
pluginManagement {
    val flutterSdkPath = run {
        val properties = java.util.Properties()
        file("local.properties").inputStream().use { properties.load(it) }
        val flutterSdkPath = properties.getProperty("flutter.sdk")
        require(flutterSdkPath != null) { "flutter.sdk not set in local.properties" }
        flutterSdkPath
    }

    includeBuild("$flutterSdkPath/packages/flutter_tools/gradle")

    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

plugins {
    id("dev.flutter.flutter-plugin-loader") version "1.0.0"
    id("com.android.application") version "8.7.3" apply false
    id("org.jetbrains.kotlin.android") version "2.1.0" apply false
}

include(":app")

```

### `frontend/android/app/build.gradle.kts`
`size: 1388 bytes`

```kts
plugins {
    id("com.android.application")
    id("kotlin-android")
    // The Flutter Gradle Plugin must be applied after the Android and Kotlin Gradle plugins.
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.example.frontend"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = flutter.ndkVersion

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    kotlinOptions {
        jvmTarget = JavaVersion.VERSION_11.toString()
    }

    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "com.example.frontend"
        // You can update the following values to match your application needs.
        // For more information, see: https://flutter.dev/to/review-gradle-config.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

    buildTypes {
        release {
            // TODO: Add your own signing config for the release build.
            // Signing with the debug keys for now, so `flutter run --release` works.
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

flutter {
    source = "../.."
}

```

### `frontend/android/app/src/profile/AndroidManifest.xml`
`size: 378 bytes`

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- The INTERNET permission is required for development. Specifically,
         the Flutter tool needs it to communicate with the running application
         to allow setting breakpoints, to provide hot reload, etc.
    -->
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest>

```

### `frontend/android/app/src/debug/AndroidManifest.xml`
`size: 378 bytes`

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- The INTERNET permission is required for development. Specifically,
         the Flutter tool needs it to communicate with the running application
         to allow setting breakpoints, to provide hot reload, etc.
    -->
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest>

```

### `frontend/android/app/src/main/AndroidManifest.xml`
`size: 2196 bytes`

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:label="frontend"
        android:name="${applicationName}"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:taskAffinity=""
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <!-- Specifies an Android theme to apply to this Activity as soon as
                 the Android process has started. This theme is visible to the user
                 while the Flutter UI initializes. After that, this theme continues
                 to determine the Window background behind the Flutter UI. -->
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"
              />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <!-- Don't delete the meta-data below.
             This is used by the Flutter tool to generate GeneratedPluginRegistrant.java -->
        <meta-data
            android:name="flutterEmbedding"
            android:value="2" />
    </application>
    <!-- Required to query activities that can process text, see:
         https://developer.android.com/training/package-visibility and
         https://developer.android.com/reference/android/content/Intent#ACTION_PROCESS_TEXT.

         In particular, this is used by the Flutter engine in io.flutter.plugin.text.ProcessTextPlugin. -->
    <queries>
        <intent>
            <action android:name="android.intent.action.PROCESS_TEXT"/>
            <data android:mimeType="text/plain"/>
        </intent>
    </queries>
</manifest>

```

### `frontend/android/app/src/main/kotlin/com/example/frontend/MainActivity.kt`
`size: 122 bytes`

```kt
package com.example.frontend

import io.flutter.embedding.android.FlutterActivity

class MainActivity : FlutterActivity()

```

### `frontend/android/app/src/main/res/drawable/launch_background.xml`
`size: 434 bytes`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Modify this file to customize your launch splash screen -->
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@android:color/white" />

    <!-- You can insert your own image assets here -->
    <!-- <item>
        <bitmap
            android:gravity="center"
            android:src="@mipmap/launch_image" />
    </item> -->
</layer-list>

```

### `frontend/android/app/src/main/res/drawable-v21/launch_background.xml`
`size: 438 bytes`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Modify this file to customize your launch splash screen -->
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="?android:colorBackground" />

    <!-- You can insert your own image assets here -->
    <!-- <item>
        <bitmap
            android:gravity="center"
            android:src="@mipmap/launch_image" />
    </item> -->
</layer-list>

```

### `frontend/android/app/src/main/res/values-night/styles.xml`
`size: 995 bytes`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Theme applied to the Android Window while the process is starting when the OS's Dark Mode setting is on -->
    <style name="LaunchTheme" parent="@android:style/Theme.Black.NoTitleBar">
        <!-- Show a splash screen on the activity. Automatically removed when
             the Flutter engine draws its first frame -->
        <item name="android:windowBackground">@drawable/launch_background</item>
    </style>
    <!-- Theme applied to the Android Window as soon as the process has started.
         This theme determines the color of the Android Window while your
         Flutter UI initializes, as well as behind your Flutter UI while its
         running.

         This Theme is only used starting with V2 of Flutter's Android embedding. -->
    <style name="NormalTheme" parent="@android:style/Theme.Black.NoTitleBar">
        <item name="android:windowBackground">?android:colorBackground</item>
    </style>
</resources>

```

### `frontend/android/app/src/main/res/values/styles.xml`
`size: 996 bytes`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Theme applied to the Android Window while the process is starting when the OS's Dark Mode setting is off -->
    <style name="LaunchTheme" parent="@android:style/Theme.Light.NoTitleBar">
        <!-- Show a splash screen on the activity. Automatically removed when
             the Flutter engine draws its first frame -->
        <item name="android:windowBackground">@drawable/launch_background</item>
    </style>
    <!-- Theme applied to the Android Window as soon as the process has started.
         This theme determines the color of the Android Window while your
         Flutter UI initializes, as well as behind your Flutter UI while its
         running.

         This Theme is only used starting with V2 of Flutter's Android embedding. -->
    <style name="NormalTheme" parent="@android:style/Theme.Light.NoTitleBar">
        <item name="android:windowBackground">?android:colorBackground</item>
    </style>
</resources>

```

### `frontend/android/gradle/wrapper/gradle-wrapper.properties`
`size: 201 bytes`

```properties
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.12-all.zip

```

### `frontend/web/index.html`
`size: 1214 bytes`

```html
<!DOCTYPE html>
<html>
<head>
  <!--
    If you are serving your web app in a path other than the root, change the
    href value below to reflect the base path you are serving from.

    The path provided below has to start and end with a slash "/" in order for
    it to work correctly.

    For more details:
    * https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base

    This is a placeholder for base href that will be replaced by the value of
    the `--base-href` argument provided to `flutter build`.
  -->
  <base href="$FLUTTER_BASE_HREF">

  <meta charset="UTF-8">
  <meta content="IE=Edge" http-equiv="X-UA-Compatible">
  <meta name="description" content="A new Flutter project.">

  <!-- iOS meta tags & icons -->
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <meta name="apple-mobile-web-app-title" content="frontend">
  <link rel="apple-touch-icon" href="icons/Icon-192.png">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="favicon.png"/>

  <title>frontend</title>
  <link rel="manifest" href="manifest.json">
</head>
<body>
  <script src="flutter_bootstrap.js" async></script>
</body>
</html>

```

### `frontend/web/manifest.json`
`size: 912 bytes`

```json
{
    "name": "frontend",
    "short_name": "frontend",
    "start_url": ".",
    "display": "standalone",
    "background_color": "#0175C2",
    "theme_color": "#0175C2",
    "description": "A new Flutter project.",
    "orientation": "portrait-primary",
    "prefer_related_applications": false,
    "icons": [
        {
            "src": "icons/Icon-192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "icons/Icon-512.png",
            "sizes": "512x512",
            "type": "image/png"
        },
        {
            "src": "icons/Icon-maskable-192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "maskable"
        },
        {
            "src": "icons/Icon-maskable-512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "maskable"
        }
    ]
}

```

### `frontend/ios/.gitignore`
`size: 569 bytes`

```
**/dgph
*.mode1v3
*.mode2v3
*.moved-aside
*.pbxuser
*.perspectivev3
**/*sync/
.sconsign.dblite
.tags*
**/.vagrant/
**/DerivedData/
Icon?
**/Pods/
**/.symlinks/
profile
xcuserdata
**/.generated/
Flutter/App.framework
Flutter/Flutter.framework
Flutter/Flutter.podspec
Flutter/Generated.xcconfig
Flutter/ephemeral/
Flutter/app.flx
Flutter/app.zip
Flutter/flutter_assets/
Flutter/flutter_export_environment.sh
ServiceDefinitions.json
Runner/GeneratedPluginRegistrant.*

# Exceptions to above rules.
!default.mode1v3
!default.mode2v3
!default.pbxuser
!default.perspectivev3

```

### `frontend/ios/Runner/AppDelegate.swift`
`size: 391 bytes`

```swift
import Flutter
import UIKit

@main
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}

```

### `frontend/ios/Runner/Info.plist`
`size: 1643 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>$(DEVELOPMENT_LANGUAGE)</string>
	<key>CFBundleDisplayName</key>
	<string>Frontend</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>frontend</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>$(FLUTTER_BUILD_NAME)</string>
	<key>CFBundleSignature</key>
	<string>????</string>
	<key>CFBundleVersion</key>
	<string>$(FLUTTER_BUILD_NUMBER)</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>UILaunchStoryboardName</key>
	<string>LaunchScreen</string>
	<key>UIMainStoryboardFile</key>
	<string>Main</string>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationPortraitUpsideDown</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>CADisableMinimumFrameDurationOnPhone</key>
	<true/>
	<key>UIApplicationSupportsIndirectInputEvents</key>
	<true/>
</dict>
</plist>

```

### `frontend/ios/Runner/Runner-Bridging-Header.h`
`size: 38 bytes`

```h
#import "GeneratedPluginRegistrant.h"

```

### `frontend/ios/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json`
`size: 2519 bytes`

```json
{
  "images" : [
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "Icon-App-20x20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "Icon-App-20x20@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "Icon-App-40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "Icon-App-40x40@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "Icon-App-60x60@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "Icon-App-60x60@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "20x20",
      "idiom" : "ipad",
      "filename" : "Icon-App-20x20@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "20x20",
      "idiom" : "ipad",
      "filename" : "Icon-App-20x20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "Icon-App-29x29@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "Icon-App-29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "Icon-App-40x40@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "Icon-App-40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "Icon-App-76x76@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "Icon-App-76x76@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "83.5x83.5",
      "idiom" : "ipad",
      "filename" : "Icon-App-83.5x83.5@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "1024x1024",
      "idiom" : "ios-marketing",
      "filename" : "Icon-App-1024x1024@1x.png",
      "scale" : "1x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}

```

### `frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset/Contents.json`
`size: 391 bytes`

```json
{
  "images" : [
    {
      "idiom" : "universal",
      "filename" : "LaunchImage.png",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "filename" : "LaunchImage@2x.png",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "filename" : "LaunchImage@3x.png",
      "scale" : "3x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}

```

### `frontend/ios/Runner/Assets.xcassets/LaunchImage.imageset/README.md`
`size: 336 bytes`

```md
# Launch Screen Assets

You can customize the launch screen with your own desired assets by replacing the image files in this directory.

You can also do it by opening your Flutter project's Xcode project with `open ios/Runner.xcworkspace`, selecting `Runner/Assets.xcassets` in the Project Navigator and dropping in the desired images.
```

### `frontend/ios/Runner/Base.lproj/LaunchScreen.storyboard`
`size: 2377 bytes`

```storyboard
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="12121" systemVersion="16G29" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" launchScreen="YES" colorMatched="YES" initialViewController="01J-lp-oVM">
    <dependencies>
        <deployment identifier="iOS"/>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="12089"/>
    </dependencies>
    <scenes>
        <!--View Controller-->
        <scene sceneID="EHf-IW-A2E">
            <objects>
                <viewController id="01J-lp-oVM" sceneMemberID="viewController">
                    <layoutGuides>
                        <viewControllerLayoutGuide type="top" id="Ydg-fD-yQy"/>
                        <viewControllerLayoutGuide type="bottom" id="xbc-2k-c8Z"/>
                    </layoutGuides>
                    <view key="view" contentMode="scaleToFill" id="Ze5-6b-2t3">
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <subviews>
                            <imageView opaque="NO" clipsSubviews="YES" multipleTouchEnabled="YES" contentMode="center" image="LaunchImage" translatesAutoresizingMaskIntoConstraints="NO" id="YRO-k0-Ey4">
                            </imageView>
                        </subviews>
                        <color key="backgroundColor" red="1" green="1" blue="1" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
                        <constraints>
                            <constraint firstItem="YRO-k0-Ey4" firstAttribute="centerX" secondItem="Ze5-6b-2t3" secondAttribute="centerX" id="1a2-6s-vTC"/>
                            <constraint firstItem="YRO-k0-Ey4" firstAttribute="centerY" secondItem="Ze5-6b-2t3" secondAttribute="centerY" id="4X2-HB-R7a"/>
                        </constraints>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="iYj-Kq-Ea1" userLabel="First Responder" sceneMemberID="firstResponder"/>
            </objects>
            <point key="canvasLocation" x="53" y="375"/>
        </scene>
    </scenes>
    <resources>
        <image name="LaunchImage" width="168" height="185"/>
    </resources>
</document>

```

### `frontend/ios/Runner/Base.lproj/Main.storyboard`
`size: 1605 bytes`

```storyboard
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="10117" systemVersion="15F34" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" useTraitCollections="YES" initialViewController="BYZ-38-t0r">
    <dependencies>
        <deployment identifier="iOS"/>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="10085"/>
    </dependencies>
    <scenes>
        <!--Flutter View Controller-->
        <scene sceneID="tne-QT-ifu">
            <objects>
                <viewController id="BYZ-38-t0r" customClass="FlutterViewController" sceneMemberID="viewController">
                    <layoutGuides>
                        <viewControllerLayoutGuide type="top" id="y3c-jy-aDJ"/>
                        <viewControllerLayoutGuide type="bottom" id="wfy-db-euE"/>
                    </layoutGuides>
                    <view key="view" contentMode="scaleToFill" id="8bC-Xf-vdC">
                        <rect key="frame" x="0.0" y="0.0" width="600" height="600"/>
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <color key="backgroundColor" white="1" alpha="1" colorSpace="custom" customColorSpace="calibratedWhite"/>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="dkx-z0-nzr" sceneMemberID="firstResponder"/>
            </objects>
        </scene>
    </scenes>
</document>

```

### `frontend/ios/Flutter/AppFrameworkInfo.plist`
`size: 774 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>App</string>
  <key>CFBundleIdentifier</key>
  <string>io.flutter.flutter.app</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>App</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>1.0</string>
  <key>MinimumOSVersion</key>
  <string>12.0</string>
</dict>
</plist>

```

### `frontend/ios/Flutter/Debug.xcconfig`
`size: 30 bytes`

```xcconfig
#include "Generated.xcconfig"

```

### `frontend/ios/Flutter/Release.xcconfig`
`size: 30 bytes`

```xcconfig
#include "Generated.xcconfig"

```

### `frontend/ios/RunnerTests/RunnerTests.swift`
`size: 285 bytes`

```swift
import Flutter
import UIKit
import XCTest

class RunnerTests: XCTestCase {

  func testExample() {
    // If you add code to the Runner application, consider adding tests here.
    // See https://developer.apple.com/documentation/xctest for more information about using XCTest.
  }

}

```

### `frontend/ios/Runner.xcodeproj/project.pbxproj`
`size: 23654 bytes`

```pbxproj
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 54;
	objects = {

/* Begin PBXBuildFile section */
		1498D2341E8E89220040F4C2 /* GeneratedPluginRegistrant.m in Sources */ = {isa = PBXBuildFile; fileRef = 1498D2331E8E89220040F4C2 /* GeneratedPluginRegistrant.m */; };
		331C808B294A63AB00263BE5 /* RunnerTests.swift in Sources */ = {isa = PBXBuildFile; fileRef = 331C807B294A618700263BE5 /* RunnerTests.swift */; };
		3B3967161E833CAA004F5970 /* AppFrameworkInfo.plist in Resources */ = {isa = PBXBuildFile; fileRef = 3B3967151E833CAA004F5970 /* AppFrameworkInfo.plist */; };
		74858FAF1ED2DC5600515810 /* AppDelegate.swift in Sources */ = {isa = PBXBuildFile; fileRef = 74858FAE1ED2DC5600515810 /* AppDelegate.swift */; };
		97C146FC1CF9000F007C117D /* Main.storyboard in Resources */ = {isa = PBXBuildFile; fileRef = 97C146FA1CF9000F007C117D /* Main.storyboard */; };
		97C146FE1CF9000F007C117D /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 97C146FD1CF9000F007C117D /* Assets.xcassets */; };
		97C147011CF9000F007C117D /* LaunchScreen.storyboard in Resources */ = {isa = PBXBuildFile; fileRef = 97C146FF1CF9000F007C117D /* LaunchScreen.storyboard */; };
/* End PBXBuildFile section */

/* Begin PBXContainerItemProxy section */
		331C8085294A63A400263BE5 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = 97C146E61CF9000F007C117D /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = 97C146ED1CF9000F007C117D;
			remoteInfo = Runner;
		};
/* End PBXContainerItemProxy section */

/* Begin PBXCopyFilesBuildPhase section */
		9705A1C41CF9048500538489 /* Embed Frameworks */ = {
			isa = PBXCopyFilesBuildPhase;
			buildActionMask = 2147483647;
			dstPath = "";
			dstSubfolderSpec = 10;
			files = (
			);
			name = "Embed Frameworks";
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXCopyFilesBuildPhase section */

/* Begin PBXFileReference section */
		1498D2321E8E86230040F4C2 /* GeneratedPluginRegistrant.h */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = GeneratedPluginRegistrant.h; sourceTree = "<group>"; };
		1498D2331E8E89220040F4C2 /* GeneratedPluginRegistrant.m */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; path = GeneratedPluginRegistrant.m; sourceTree = "<group>"; };
		331C807B294A618700263BE5 /* RunnerTests.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RunnerTests.swift; sourceTree = "<group>"; };
		331C8081294A63A400263BE5 /* RunnerTests.xctest */ = {isa = PBXFileReference; explicitFileType = wrapper.cfbundle; includeInIndex = 0; path = RunnerTests.xctest; sourceTree = BUILT_PRODUCTS_DIR; };
		3B3967151E833CAA004F5970 /* AppFrameworkInfo.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; name = AppFrameworkInfo.plist; path = Flutter/AppFrameworkInfo.plist; sourceTree = "<group>"; };
		74858FAD1ED2DC5600515810 /* Runner-Bridging-Header.h */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = "Runner-Bridging-Header.h"; sourceTree = "<group>"; };
		74858FAE1ED2DC5600515810 /* AppDelegate.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = AppDelegate.swift; sourceTree = "<group>"; };
		7AFA3C8E1D35360C0083082E /* Release.xcconfig */ = {isa = PBXFileReference; lastKnownFileType = text.xcconfig; name = Release.xcconfig; path = Flutter/Release.xcconfig; sourceTree = "<group>"; };
		9740EEB21CF90195004384FC /* Debug.xcconfig */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.xcconfig; name = Debug.xcconfig; path = Flutter/Debug.xcconfig; sourceTree = "<group>"; };
		9740EEB31CF90195004384FC /* Generated.xcconfig */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.xcconfig; name = Generated.xcconfig; path = Flutter/Generated.xcconfig; sourceTree = "<group>"; };
		97C146EE1CF9000F007C117D /* Runner.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = Runner.app; sourceTree = BUILT_PRODUCTS_DIR; };
		97C146FB1CF9000F007C117D /* Base */ = {isa = PBXFileReference; lastKnownFileType = file.storyboard; name = Base; path = Base.lproj/Main.storyboard; sourceTree = "<group>"; };
		97C146FD1CF9000F007C117D /* Assets.xcassets */ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; };
		97C147001CF9000F007C117D /* Base */ = {isa = PBXFileReference; lastKnownFileType = file.storyboard; name = Base; path = Base.lproj/LaunchScreen.storyboard; sourceTree = "<group>"; };
		97C147021CF9000F007C117D /* Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		97C146EB1CF9000F007C117D /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		331C8082294A63A400263BE5 /* RunnerTests */ = {
			isa = PBXGroup;
			children = (
				331C807B294A618700263BE5 /* RunnerTests.swift */,
			);
			path = RunnerTests;
			sourceTree = "<group>";
		};
		9740EEB11CF90186004384FC /* Flutter */ = {
			isa = PBXGroup;
			children = (
				3B3967151E833CAA004F5970 /* AppFrameworkInfo.plist */,
				9740EEB21CF90195004384FC /* Debug.xcconfig */,
				7AFA3C8E1D35360C0083082E /* Release.xcconfig */,
				9740EEB31CF90195004384FC /* Generated.xcconfig */,
			);
			name = Flutter;
			sourceTree = "<group>";
		};
		97C146E51CF9000F007C117D = {
			isa = PBXGroup;
			children = (
				9740EEB11CF90186004384FC /* Flutter */,
				97C146F01CF9000F007C117D /* Runner */,
				97C146EF1CF9000F007C117D /* Products */,
				331C8082294A63A400263BE5 /* RunnerTests */,
			);
			sourceTree = "<group>";
		};
		97C146EF1CF9000F007C117D /* Products */ = {
			isa = PBXGroup;
			children = (
				97C146EE1CF9000F007C117D /* Runner.app */,
				331C8081294A63A400263BE5 /* RunnerTests.xctest */,
			);
			name = Products;
			sourceTree = "<group>";
		};
		97C146F01CF9000F007C117D /* Runner */ = {
			isa = PBXGroup;
			children = (
				97C146FA1CF9000F007C117D /* Main.storyboard */,
				97C146FD1CF9000F007C117D /* Assets.xcassets */,
				97C146FF1CF9000F007C117D /* LaunchScreen.storyboard */,
				97C147021CF9000F007C117D /* Info.plist */,
				1498D2321E8E86230040F4C2 /* GeneratedPluginRegistrant.h */,
				1498D2331E8E89220040F4C2 /* GeneratedPluginRegistrant.m */,
				74858FAE1ED2DC5600515810 /* AppDelegate.swift */,
				74858FAD1ED2DC5600515810 /* Runner-Bridging-Header.h */,
			);
			path = Runner;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		331C8080294A63A400263BE5 /* RunnerTests */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 331C8087294A63A400263BE5 /* Build configuration list for PBXNativeTarget "RunnerTests" */;
			buildPhases = (
				331C807D294A63A400263BE5 /* Sources */,
				331C807F294A63A400263BE5 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
				331C8086294A63A400263BE5 /* PBXTargetDependency */,
			);
			name = RunnerTests;
			productName = RunnerTests;
			productReference = 331C8081294A63A400263BE5 /* RunnerTests.xctest */;
			productType = "com.apple.product-type.bundle.unit-test";
		};
		97C146ED1CF9000F007C117D /* Runner */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 97C147051CF9000F007C117D /* Build configuration list for PBXNativeTarget "Runner" */;
			buildPhases = (
				9740EEB61CF901F6004384FC /* Run Script */,
				97C146EA1CF9000F007C117D /* Sources */,
				97C146EB1CF9000F007C117D /* Frameworks */,
				97C146EC1CF9000F007C117D /* Resources */,
				9705A1C41CF9048500538489 /* Embed Frameworks */,
				3B06AD1E1E4923F5004D2608 /* Thin Binary */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = Runner;
			productName = Runner;
			productReference = 97C146EE1CF9000F007C117D /* Runner.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		97C146E61CF9000F007C117D /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = YES;
				LastUpgradeCheck = 1510;
				ORGANIZATIONNAME = "";
				TargetAttributes = {
					331C8080294A63A400263BE5 = {
						CreatedOnToolsVersion = 14.0;
						TestTargetID = 97C146ED1CF9000F007C117D;
					};
					97C146ED1CF9000F007C117D = {
						CreatedOnToolsVersion = 7.3.1;
						LastSwiftMigration = 1100;
					};
				};
			};
			buildConfigurationList = 97C146E91CF9000F007C117D /* Build configuration list for PBXProject "Runner" */;
			compatibilityVersion = "Xcode 9.3";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 97C146E51CF9000F007C117D;
			productRefGroup = 97C146EF1CF9000F007C117D /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				97C146ED1CF9000F007C117D /* Runner */,
				331C8080294A63A400263BE5 /* RunnerTests */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		331C807F294A63A400263BE5 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		97C146EC1CF9000F007C117D /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				97C147011CF9000F007C117D /* LaunchScreen.storyboard in Resources */,
				3B3967161E833CAA004F5970 /* AppFrameworkInfo.plist in Resources */,
				97C146FE1CF9000F007C117D /* Assets.xcassets in Resources */,
				97C146FC1CF9000F007C117D /* Main.storyboard in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXShellScriptBuildPhase section */
		3B06AD1E1E4923F5004D2608 /* Thin Binary */ = {
			isa = PBXShellScriptBuildPhase;
			alwaysOutOfDate = 1;
			buildActionMask = 2147483647;
			files = (
			);
			inputPaths = (
				"${TARGET_BUILD_DIR}/${INFOPLIST_PATH}",
			);
			name = "Thin Binary";
			outputPaths = (
			);
			runOnlyForDeploymentPostprocessing = 0;
			shellPath = /bin/sh;
			shellScript = "/bin/sh \"$FLUTTER_ROOT/packages/flutter_tools/bin/xcode_backend.sh\" embed_and_thin";
		};
		9740EEB61CF901F6004384FC /* Run Script */ = {
			isa = PBXShellScriptBuildPhase;
			alwaysOutOfDate = 1;
			buildActionMask = 2147483647;
			files = (
			);
			inputPaths = (
			);
			name = "Run Script";
			outputPaths = (
			);
			runOnlyForDeploymentPostprocessing = 0;
			shellPath = /bin/sh;
			shellScript = "/bin/sh \"$FLUTTER_ROOT/packages/flutter_tools/bin/xcode_backend.sh\" build";
		};
/* End PBXShellScriptBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		331C807D294A63A400263BE5 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				331C808B294A63AB00263BE5 /* RunnerTests.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		97C146EA1CF9000F007C117D /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				74858FAF1ED2DC5600515810 /* AppDelegate.swift in Sources */,
				1498D2341E8E89220040F4C2 /* GeneratedPluginRegistrant.m in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin PBXTargetDependency section */
		331C8086294A63A400263BE5 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = 97C146ED1CF9000F007C117D /* Runner */;
			targetProxy = 331C8085294A63A400263BE5 /* PBXContainerItemProxy */;
		};
/* End PBXTargetDependency section */

/* Begin PBXVariantGroup section */
		97C146FA1CF9000F007C117D /* Main.storyboard */ = {
			isa = PBXVariantGroup;
			children = (
				97C146FB1CF9000F007C117D /* Base */,
			);
			name = Main.storyboard;
			sourceTree = "<group>";
		};
		97C146FF1CF9000F007C117D /* LaunchScreen.storyboard */ = {
			isa = PBXVariantGroup;
			children = (
				97C147001CF9000F007C117D /* Base */,
			);
			name = LaunchScreen.storyboard;
			sourceTree = "<group>";
		};
/* End PBXVariantGroup section */

/* Begin XCBuildConfiguration section */
		249021D3217E4FDB00AE95B9 /* Profile */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++0x";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone Developer";
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = NO;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				SDKROOT = iphoneos;
				SUPPORTED_PLATFORMS = iphoneos;
				TARGETED_DEVICE_FAMILY = "1,2";
				VALIDATE_PRODUCT = YES;
			};
			name = Profile;
		};
		249021D4217E4FDB00AE95B9 /* Profile */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 7AFA3C8E1D35360C0083082E /* Release.xcconfig */;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CLANG_ENABLE_MODULES = YES;
				CURRENT_PROJECT_VERSION = "$(FLUTTER_BUILD_NUMBER)";
				ENABLE_BITCODE = NO;
				INFOPLIST_FILE = Runner/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_OBJC_BRIDGING_HEADER = "Runner/Runner-Bridging-Header.h";
				SWIFT_VERSION = 5.0;
				VERSIONING_SYSTEM = "apple-generic";
			};
			name = Profile;
		};
		331C8088294A63A400263BE5 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend.RunnerTests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				SWIFT_VERSION = 5.0;
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/Runner.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/Runner";
			};
			name = Debug;
		};
		331C8089294A63A400263BE5 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend.RunnerTests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_VERSION = 5.0;
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/Runner.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/Runner";
			};
			name = Release;
		};
		331C808A294A63A400263BE5 /* Profile */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend.RunnerTests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_VERSION = 5.0;
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/Runner.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/Runner";
			};
			name = Profile;
		};
		97C147031CF9000F007C117D /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++0x";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone Developer";
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = NO;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				MTL_ENABLE_DEBUG_INFO = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		97C147041CF9000F007C117D /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++0x";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone Developer";
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = NO;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 12.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				SDKROOT = iphoneos;
				SUPPORTED_PLATFORMS = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				TARGETED_DEVICE_FAMILY = "1,2";
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		97C147061CF9000F007C117D /* Debug */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 9740EEB21CF90195004384FC /* Debug.xcconfig */;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CLANG_ENABLE_MODULES = YES;
				CURRENT_PROJECT_VERSION = "$(FLUTTER_BUILD_NUMBER)";
				ENABLE_BITCODE = NO;
				INFOPLIST_FILE = Runner/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_OBJC_BRIDGING_HEADER = "Runner/Runner-Bridging-Header.h";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				SWIFT_VERSION = 5.0;
				VERSIONING_SYSTEM = "apple-generic";
			};
			name = Debug;
		};
		97C147071CF9000F007C117D /* Release */ = {
			isa = XCBuildConfiguration;
			baseConfigurationReference = 7AFA3C8E1D35360C0083082E /* Release.xcconfig */;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CLANG_ENABLE_MODULES = YES;
				CURRENT_PROJECT_VERSION = "$(FLUTTER_BUILD_NUMBER)";
				ENABLE_BITCODE = NO;
				INFOPLIST_FILE = Runner/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				PRODUCT_BUNDLE_IDENTIFIER = com.example.frontend;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_OBJC_BRIDGING_HEADER = "Runner/Runner-Bridging-Header.h";
				SWIFT_VERSION = 5.0;
				VERSIONING_SYSTEM = "apple-generic";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		331C8087294A63A400263BE5 /* Build configuration list for PBXNativeTarget "RunnerTests" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				331C8088294A63A400263BE5 /* Debug */,
				331C8089294A63A400263BE5 /* Release */,
				331C808A294A63A400263BE5 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		97C146E91CF9000F007C117D /* Build configuration list for PBXProject "Runner" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				97C147031CF9000F007C117D /* Debug */,
				97C147041CF9000F007C117D /* Release */,
				249021D3217E4FDB00AE95B9 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		97C147051CF9000F007C117D /* Build configuration list for PBXNativeTarget "Runner" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				97C147061CF9000F007C117D /* Debug */,
				97C147071CF9000F007C117D /* Release */,
				249021D4217E4FDB00AE95B9 /* Profile */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 97C146E61CF9000F007C117D /* Project object */;
}

```

### `frontend/ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme`
`size: 3833 bytes`

```xcscheme
<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "1510"
   version = "1.3">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "97C146ED1CF9000F007C117D"
               BuildableName = "Runner.app"
               BlueprintName = "Runner"
               ReferencedContainer = "container:Runner.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      customLLDBInitFile = "$(SRCROOT)/Flutter/ephemeral/flutter_lldbinit"
      shouldUseLaunchSchemeArgsEnv = "YES">
      <MacroExpansion>
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "97C146ED1CF9000F007C117D"
            BuildableName = "Runner.app"
            BlueprintName = "Runner"
            ReferencedContainer = "container:Runner.xcodeproj">
         </BuildableReference>
      </MacroExpansion>
      <Testables>
         <TestableReference
            skipped = "NO"
            parallelizable = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "331C8080294A63A400263BE5"
               BuildableName = "RunnerTests.xctest"
               BlueprintName = "RunnerTests"
               ReferencedContainer = "container:Runner.xcodeproj">
            </BuildableReference>
         </TestableReference>
      </Testables>
   </TestAction>
   <LaunchAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      customLLDBInitFile = "$(SRCROOT)/Flutter/ephemeral/flutter_lldbinit"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      enableGPUValidationMode = "1"
      allowLocationSimulation = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "97C146ED1CF9000F007C117D"
            BuildableName = "Runner.app"
            BlueprintName = "Runner"
            ReferencedContainer = "container:Runner.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </LaunchAction>
   <ProfileAction
      buildConfiguration = "Profile"
      shouldUseLaunchSchemeArgsEnv = "YES"
      savedToolIdentifier = ""
      useCustomWorkingDirectory = "NO"
      debugDocumentVersioning = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "97C146ED1CF9000F007C117D"
            BuildableName = "Runner.app"
            BlueprintName = "Runner"
            ReferencedContainer = "container:Runner.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction
      buildConfiguration = "Debug">
   </AnalyzeAction>
   <ArchiveAction
      buildConfiguration = "Release"
      revealArchiveInOrganizer = "YES">
   </ArchiveAction>
</Scheme>

```

### `frontend/ios/Runner.xcodeproj/project.xcworkspace/contents.xcworkspacedata`
`size: 135 bytes`

```xcworkspacedata
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:">
   </FileRef>
</Workspace>

```

### `frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist`
`size: 238 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>IDEDidComputeMac32BitWarning</key>
	<true/>
</dict>
</plist>

```

### `frontend/ios/Runner.xcodeproj/project.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings`
`size: 226 bytes`

```xcsettings
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PreviewsEnabled</key>
	<false/>
</dict>
</plist>

```

### `frontend/ios/Runner.xcworkspace/contents.xcworkspacedata`
`size: 152 bytes`

```xcworkspacedata
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "group:Runner.xcodeproj">
   </FileRef>
</Workspace>

```

### `frontend/ios/Runner.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist`
`size: 238 bytes`

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>IDEDidComputeMac32BitWarning</key>
	<true/>
</dict>
</plist>

```

### `frontend/ios/Runner.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings`
`size: 226 bytes`

```xcsettings
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PreviewsEnabled</key>
	<false/>
</dict>
</plist>

```

### `frontend/test/widget_test.dart`
`size: 1059 bytes`

```dart
// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:frontend/main.dart';

void main() {
  testWidgets('Counter increments smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());

    // Verify that our counter starts at 0.
    expect(find.text('0'), findsOneWidget);
    expect(find.text('1'), findsNothing);

    // Tap the '+' icon and trigger a frame.
    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();

    // Verify that our counter has incremented.
    expect(find.text('0'), findsNothing);
    expect(find.text('1'), findsOneWidget);
  });
}

```

### `frontend/lib/main.dart`
`size: 1214 bytes`

```dart
// import 'package:flutter/material.dart';
// import 'screens/login_screen.dart';
// import 'screens/home_screen.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'AILEE',
//       initialRoute: '/login',
//       routes: {
//         '/login': (context) => const LoginScreen(),
//         '/home': (context) => const HomeScreen(),
//       },
//     );
//   }
// }

import 'package:flutter/material.dart';
import 'screens/login_screen.dart';
import 'screens/home_screen.dart';
import 'screens/menu/ai_home_menu.dart'; // ✅ 추가

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AILEE',
      debugShowCheckedModeBanner: false,
      initialRoute: '/login',
      routes: {
        '/login': (context) => const LoginScreen(),
        '/home': (context) => const HomeScreen(),
        '/menu': (context) => const AIHomeMenu(), // ✅ 메뉴 라우트 추가
      },
    );
  }
}

```

### `frontend/lib/screens/ai_monitor.dart`
`size: 3712 bytes`

```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:fl_chart/fl_chart.dart';

class AIMonitorScreen extends StatefulWidget {
  const AIMonitorScreen({Key? key}) : super(key: key);

  @override
  State<AIMonitorScreen> createState() => _AIMonitorScreenState();
}

class _AIMonitorScreenState extends State<AIMonitorScreen> {
  List<FlSpot> actualData = [];
  List<FlSpot> predictedData = [];
  bool isLoading = false;
  String statusMessage = "";

  int counter = 0; // X축 데이터 인덱스

  Future<void> fetchPrediction() async {
    setState(() => isLoading = true);

    try {
      // final url = Uri.parse("http://127.0.0.1:8000/predict?plant_id=01&res_id=EQP01&tag_name=OIL_TEMP_ACT&value=40.5");
      final url = Uri.parse(
          "http://127.0.0.1:8000/predict?plant_id=01&res_id=59-066&tag_name=S3_TEMP");
      final response = await http.get(url);

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));

        double actual = data["input_value"] ?? 0;
        double predicted = data["predicted_value"] ?? 0;
        bool isAnomaly = (data["is_anomaly"] == "Y");

        setState(() {
          actualData.add(FlSpot(counter.toDouble(), actual));
          predictedData.add(FlSpot(counter.toDouble(), predicted));
          counter++;

          statusMessage = isAnomaly ? "⚠ 이상 발생!" : "정상 상태";
        });
      } else {
        setState(() => statusMessage = "❌ 서버 오류");
      }
    } catch (e) {
      setState(() => statusMessage = "🔥 연결 실패: $e");
    } finally {
      setState(() => isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("⚠ AI 이상 감지")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: isLoading ? null : fetchPrediction,
              child: isLoading
                  ? const CircularProgressIndicator(color: Colors.white)
                  : const Text("예측 실행"),
            ),
            const SizedBox(height: 12),
            Text(
              statusMessage,
              style: TextStyle(
                fontSize: 18,
                color: statusMessage.contains("이상") ? Colors.red : Colors.green,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: LineChart(
                LineChartData(
                  titlesData: FlTitlesData(
                    leftTitles: AxisTitles(
                      sideTitles:
                          SideTitles(showTitles: true, reservedSize: 40),
                    ),
                    bottomTitles: AxisTitles(
                      sideTitles: SideTitles(showTitles: true),
                    ),
                  ),
                  lineBarsData: [
                    LineChartBarData(
                      spots: actualData,
                      isCurved: true,
                      color: Colors.blue,
                      barWidth: 3,
                      dotData: FlDotData(show: true),
                    ),
                    LineChartBarData(
                      spots: predictedData,
                      isCurved: true,
                      color: Colors.red,
                      barWidth: 3,
                      dotData: FlDotData(show: true),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

```

### `frontend/lib/screens/home_screen.dart`
`size: 1386 bytes`

```dart
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // 로그인에서 전달된 데이터 받기
    final arguments = ModalRoute.of(context)?.settings.arguments;

    return Scaffold(
      appBar: AppBar(title: const Text('AILEE HOME'), centerTitle: true),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'go',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 16),

            // Text(
            //   '받은 데이터: ${arguments.toString()}',
            //   style: const TextStyle(fontSize: 16),
            // ),
            const SizedBox(height: 32),

            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/menu'); // ✅ AI 홈 메뉴로 이동
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(
                  horizontal: 32,
                  vertical: 16,
                ),
              ),
              child: const Text('AI 메뉴로 이동', style: TextStyle(fontSize: 18)),
            ),
          ],
        ),
      ),
    );
  }
}

```

### `frontend/lib/screens/login_screen.dart`
`size: 6690 bytes`

```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _idController = TextEditingController();
  final TextEditingController _pwController = TextEditingController();
  final FocusNode _pwFocusNode = FocusNode(); // ✅ 포커스 노드

  String _errorMessage = '';
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _checkAutoLogin();
  }

  Future<void> _checkAutoLogin() async {
    final prefs = await SharedPreferences.getInstance();
    final isLoggedIn = prefs.getBool('is_logged_in') ?? false;
    final savedUserId = prefs.getString('user_id');
    final savedUserName = prefs.getString('user_name');

    if (isLoggedIn && savedUserId != null && savedUserId.isNotEmpty) {
      Navigator.pushReplacementNamed(
        context,
        '/menu',
        arguments: {
          'user_id': savedUserId,
          'user_name': savedUserName ?? savedUserId,
        },
      );
    }
  }

  Future<void> _login() async {
    FocusScope.of(context).unfocus(); // 키보드 닫기
    setState(() {
      _isLoading = true;
      _errorMessage = '';
    });

    try {
      final url = Uri.parse('http://127.0.0.1:8000/auth/login');
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'user_id': _idController.text.trim(),
          'password': _pwController.text.trim(),
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));

        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('user_id', data['user_id']);
        await prefs.setString('user_name', data['user_name']);
        await prefs.setBool('is_logged_in', true);

        Navigator.pushReplacementNamed(context, '/menu', arguments: data);
      } else {
        final err = jsonDecode(utf8.decode(response.bodyBytes));
        setState(() {
          _errorMessage = err['detail'] ?? '로그인 실패';
        });
      }
    } catch (e) {
      setState(() {
        _errorMessage = '서버에 연결할 수 없습니다.';
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  void dispose() {
    _idController.dispose();
    _pwController.dispose();
    _pwFocusNode.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;
    final double logoSize = screenWidth < 600 ? 60 : 100;

    return Scaffold(
      backgroundColor: const Color(0xFFF9F9FB),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24),
          child: Container(
            constraints: const BoxConstraints(maxWidth: 400),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                // ✅ 로고 + 제목
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.asset(
                      'assets/logo/CH_2.png',
                      width: logoSize,
                      height: logoSize,
                      fit: BoxFit.contain,
                    ),
                    const SizedBox(width: 12),
                    const Text(
                      '창현이의 AI 로그인',
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 32),

                // ✅ 아이디 입력
                TextField(
                  controller: _idController,
                  enabled: !_isLoading,
                  textInputAction: TextInputAction.next,
                  onSubmitted: (_) =>
                      FocusScope.of(context).requestFocus(_pwFocusNode),
                  decoration: InputDecoration(
                    labelText: '계정',
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                    filled: true,
                    fillColor: Colors.white,
                  ),
                ),

                const SizedBox(height: 16),

                // ✅ 비밀번호 입력
                TextField(
                  controller: _pwController,
                  focusNode: _pwFocusNode,
                  enabled: !_isLoading,
                  obscureText: true,
                  textInputAction: TextInputAction.done,
                  onSubmitted: (_) => !_isLoading ? _login() : null,
                  decoration: InputDecoration(
                    labelText: '비밀번호',
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                    filled: true,
                    fillColor: Colors.white,
                  ),
                ),

                const SizedBox(height: 16),

                // ✅ 에러 메시지
                if (_errorMessage.isNotEmpty)
                  Text(
                    _errorMessage,
                    style: const TextStyle(color: Colors.red, fontSize: 14),
                  ),

                const SizedBox(height: 24),

                // ✅ 로그인 버튼
                SizedBox(
                  width: double.infinity,
                  height: 50,
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blueAccent,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
                    onPressed: _isLoading ? null : _login,
                    child: _isLoading
                        ? const CircularProgressIndicator(color: Colors.white)
                        : const Text('로그인', style: TextStyle(fontSize: 18)),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

```

### `frontend/lib/screens/menu/ai_home_menu.dart`
`size: 3525 bytes`

```dart
// D:\Web_AI_Temp\frontend\lib\screens\menu\ai_home_menu.dart
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:frontend/screens/menu/anomaly_screen.dart';

class AIHomeMenu extends StatelessWidget {
  const AIHomeMenu({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4,
      child: Scaffold(
        extendBodyBehindAppBar: true,
        backgroundColor: const Color(0xFFF3F4F6),
        appBar: PreferredSize(
          preferredSize: const Size.fromHeight(100),
          child: ClipRRect(
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 12, sigmaY: 12),
              child: AppBar(
                backgroundColor: Colors.white.withOpacity(0.85),
                elevation: 6,
                shape: const RoundedRectangleBorder(
                  borderRadius:
                      BorderRadius.vertical(bottom: Radius.circular(16)),
                ),
                title: const Text(
                  '٩(๑•̀ㅂ•́)و AI Monitoring System',
                  style: TextStyle(
                    color: Color(0xFF1F2937),
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                    letterSpacing: 0.8,
                  ),
                ),
                centerTitle: true,
                bottom: const TabBar(
                  isScrollable: false,
                  indicator: UnderlineTabIndicator(
                    borderSide:
                        BorderSide(width: 4.0, color: Color(0xFF7C3AED)),
                    insets: EdgeInsets.symmetric(horizontal: 16),
                  ),
                  labelColor: Color(0xFF7C3AED),
                  unselectedLabelColor: Colors.grey,
                  labelStyle: TextStyle(fontWeight: FontWeight.bold),
                  tabs: [
                    Tab(
                        icon: Icon(Icons.warning_amber_rounded),
                        text: "AI 이상 감지"),
                    Tab(icon: Icon(Icons.trending_up), text: "실시간 추이"),
                    Tab(icon: Icon(Icons.insights), text: "히스토그램"),
                    Tab(icon: Icon(Icons.settings), text: "설정"),
                  ],
                ),
              ),
            ),
          ),
        ),
        body: const TabBarView(
          children: [
            AnomalyScreen(), // ⬅️ 순서 변경
            _PlaceholderPage("📈 실시간 추이 페이지", Colors.indigo),
            _PlaceholderPage("📊 히스토그램 페이지", Colors.deepOrange),
            _PlaceholderPage("⚙️ 설정 페이지", Colors.teal),
          ],
        ),
      ),
    );
  }
}

class _PlaceholderPage extends StatelessWidget {
  final String text;
  final Color color;

  const _PlaceholderPage(this.text, this.color, {super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.center,
      child: Card(
        elevation: 8,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        color: color.withOpacity(0.1),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 40),
          child: Text(
            text,
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: color,
              letterSpacing: 1.1,
            ),
          ),
        ),
      ),
    );
  }
}

```

### `frontend/lib/screens/menu/anomaly_screen.dart`
`size: 3340 bytes`

```dart
// D:\Web_AI_Temp\frontend\lib\screens\menu\anomaly_screen.dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:fl_chart/fl_chart.dart';

class AnomalyScreen extends StatefulWidget {
  const AnomalyScreen({super.key});

  @override
  State<AnomalyScreen> createState() => _AnomalyScreenState();
}

class _AnomalyScreenState extends State<AnomalyScreen> {
  bool _loading = false;
  double? _predictedValue;
  String? _isAnomaly;

  Future<void> _fetchPrediction() async {
    setState(() => _loading = true);

    try {
      final url = Uri.parse(
        "http://127.0.0.1:8000/predict?plant_id=01&res_id=59-066&tag_name=S3_TEMP",
      );

      final response = await http.get(url);

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));

        setState(() {
          _predictedValue = data["predicted_value"];
          _isAnomaly = data["is_anomaly"];
        });
      } else {
        setState(() {
          _predictedValue = null;
          _isAnomaly = "오류 발생";
        });
      }
    } catch (e) {
      setState(() {
        _predictedValue = null;
        _isAnomaly = "서버 연결 실패";
      });
    } finally {
      setState(() => _loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:
          AppBar(title: const Text("창현이의 AI 이상 감지 ‧⁺◟( ᵒ̴̶̷̥́ ·̫ ᵒ̴̶̷̣̥̀ ) ")),
      body: Center(
        child: _loading
            ? const CircularProgressIndicator()
            : Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                    onPressed: _fetchPrediction,
                    child: const Text("AI 예측 실행"),
                  ),
                  const SizedBox(height: 20),
                  if (_predictedValue != null) ...[
                    Text(
                      "예측값: $_predictedValue",
                      style: const TextStyle(fontSize: 18),
                    ),
                    Text(
                      "이상 여부: $_isAnomaly",
                      style: TextStyle(
                        fontSize: 18,
                        color: _isAnomaly == "Y" ? Colors.red : Colors.green,
                      ),
                    ),
                    const SizedBox(height: 30),
                    SizedBox(
                      height: 200,
                      child: BarChart(
                        BarChartData(
                          alignment: BarChartAlignment.center,
                          barGroups: [
                            BarChartGroupData(
                              x: 0,
                              barRods: [
                                BarChartRodData(
                                  toY: _predictedValue ?? 0,
                                  color: Colors.blue,
                                  width: 30,
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ],
              ),
      ),
    );
  }
}

```

### `frontend/lib/screens/menu/histogram_screen.dart`
`size: 0 bytes`

```dart

```

### `frontend/lib/screens/menu/trend_screen.dart`
`size: 0 bytes`

```dart

```

### `frontend/lib/services/api_service.dart`
`size: 1164 bytes`

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://127.0.0.1:8000"; // 백엔드 URL

  // 로그인 API
  static Future<Map<String, dynamic>> login(
    String userId,
    String password,
  ) async {
    final url = Uri.parse("$baseUrl/auth/login");
    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"user_id": userId, "password": password}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception(jsonDecode(response.body)['detail'] ?? "로그인 실패");
    }
  }

  // 예측 API
  static Future<Map<String, dynamic>> getPrediction(
    String plantId,
    String resId,
    String tagName,
    double value,
  ) async {
    final url = Uri.parse(
      "$baseUrl/predict/?plant_id=$plantId&res_id=$resId&tag_name=$tagName&value=$value",
    );
    final response = await http.get(url);

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception("예측 API 호출 실패");
    }
  }
}

```

### `frontend/linux/.gitignore`
`size: 18 bytes`

```
flutter/ephemeral

```

### `frontend/linux/CMakeLists.txt`
`size: 4755 bytes`

```txt
# Project-level configuration.
cmake_minimum_required(VERSION 3.13)
project(runner LANGUAGES CXX)

# The name of the executable created for the application. Change this to change
# the on-disk name of your application.
set(BINARY_NAME "frontend")
# The unique GTK application identifier for this application. See:
# https://wiki.gnome.org/HowDoI/ChooseApplicationID
set(APPLICATION_ID "com.example.frontend")

# Explicitly opt in to modern CMake behaviors to avoid warnings with recent
# versions of CMake.
cmake_policy(SET CMP0063 NEW)

# Load bundled libraries from the lib/ directory relative to the binary.
set(CMAKE_INSTALL_RPATH "$ORIGIN/lib")

# Root filesystem for cross-building.
if(FLUTTER_TARGET_PLATFORM_SYSROOT)
  set(CMAKE_SYSROOT ${FLUTTER_TARGET_PLATFORM_SYSROOT})
  set(CMAKE_FIND_ROOT_PATH ${CMAKE_SYSROOT})
  set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
  set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
  set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
  set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
endif()

# Define build configuration options.
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE "Debug" CACHE
    STRING "Flutter build mode" FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS
    "Debug" "Profile" "Release")
endif()

# Compilation settings that should be applied to most targets.
#
# Be cautious about adding new options here, as plugins use this function by
# default. In most cases, you should add new options to specific targets instead
# of modifying this function.
function(APPLY_STANDARD_SETTINGS TARGET)
  target_compile_features(${TARGET} PUBLIC cxx_std_14)
  target_compile_options(${TARGET} PRIVATE -Wall -Werror)
  target_compile_options(${TARGET} PRIVATE "$<$<NOT:$<CONFIG:Debug>>:-O3>")
  target_compile_definitions(${TARGET} PRIVATE "$<$<NOT:$<CONFIG:Debug>>:NDEBUG>")
endfunction()

# Flutter library and tool build rules.
set(FLUTTER_MANAGED_DIR "${CMAKE_CURRENT_SOURCE_DIR}/flutter")
add_subdirectory(${FLUTTER_MANAGED_DIR})

# System-level dependencies.
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK REQUIRED IMPORTED_TARGET gtk+-3.0)

# Application build; see runner/CMakeLists.txt.
add_subdirectory("runner")

# Run the Flutter tool portions of the build. This must not be removed.
add_dependencies(${BINARY_NAME} flutter_assemble)

# Only the install-generated bundle's copy of the executable will launch
# correctly, since the resources must in the right relative locations. To avoid
# people trying to run the unbundled copy, put it in a subdirectory instead of
# the default top-level location.
set_target_properties(${BINARY_NAME}
  PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/intermediates_do_not_run"
)


# Generated plugin build rules, which manage building the plugins and adding
# them to the application.
include(flutter/generated_plugins.cmake)


# === Installation ===
# By default, "installing" just makes a relocatable bundle in the build
# directory.
set(BUILD_BUNDLE_DIR "${PROJECT_BINARY_DIR}/bundle")
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX "${BUILD_BUNDLE_DIR}" CACHE PATH "..." FORCE)
endif()

# Start with a clean build bundle directory every time.
install(CODE "
  file(REMOVE_RECURSE \"${BUILD_BUNDLE_DIR}/\")
  " COMPONENT Runtime)

set(INSTALL_BUNDLE_DATA_DIR "${CMAKE_INSTALL_PREFIX}/data")
set(INSTALL_BUNDLE_LIB_DIR "${CMAKE_INSTALL_PREFIX}/lib")

install(TARGETS ${BINARY_NAME} RUNTIME DESTINATION "${CMAKE_INSTALL_PREFIX}"
  COMPONENT Runtime)

install(FILES "${FLUTTER_ICU_DATA_FILE}" DESTINATION "${INSTALL_BUNDLE_DATA_DIR}"
  COMPONENT Runtime)

install(FILES "${FLUTTER_LIBRARY}" DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
  COMPONENT Runtime)

foreach(bundled_library ${PLUGIN_BUNDLED_LIBRARIES})
  install(FILES "${bundled_library}"
    DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
    COMPONENT Runtime)
endforeach(bundled_library)

# Copy the native assets provided by the build.dart from all packages.
set(NATIVE_ASSETS_DIR "${PROJECT_BUILD_DIR}native_assets/linux/")
install(DIRECTORY "${NATIVE_ASSETS_DIR}"
   DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
   COMPONENT Runtime)

# Fully re-copy the assets directory on each build to avoid having stale files
# from a previous install.
set(FLUTTER_ASSET_DIR_NAME "flutter_assets")
install(CODE "
  file(REMOVE_RECURSE \"${INSTALL_BUNDLE_DATA_DIR}/${FLUTTER_ASSET_DIR_NAME}\")
  " COMPONENT Runtime)
install(DIRECTORY "${PROJECT_BUILD_DIR}/${FLUTTER_ASSET_DIR_NAME}"
  DESTINATION "${INSTALL_BUNDLE_DATA_DIR}" COMPONENT Runtime)

# Install the AOT library on non-Debug builds only.
if(NOT CMAKE_BUILD_TYPE MATCHES "Debug")
  install(FILES "${AOT_LIBRARY}" DESTINATION "${INSTALL_BUNDLE_LIB_DIR}"
    COMPONENT Runtime)
endif()

```

### `frontend/linux/runner/CMakeLists.txt`
`size: 974 bytes`

```txt
cmake_minimum_required(VERSION 3.13)
project(runner LANGUAGES CXX)

# Define the application target. To change its name, change BINARY_NAME in the
# top-level CMakeLists.txt, not the value here, or `flutter run` will no longer
# work.
#
# Any new source files that you add to the application should be added here.
add_executable(${BINARY_NAME}
  "main.cc"
  "my_application.cc"
  "${FLUTTER_MANAGED_DIR}/generated_plugin_registrant.cc"
)

# Apply the standard set of build settings. This can be removed for applications
# that need different build settings.
apply_standard_settings(${BINARY_NAME})

# Add preprocessor definitions for the application ID.
add_definitions(-DAPPLICATION_ID="${APPLICATION_ID}")

# Add dependency libraries. Add any application-specific dependencies here.
target_link_libraries(${BINARY_NAME} PRIVATE flutter)
target_link_libraries(${BINARY_NAME} PRIVATE PkgConfig::GTK)

target_include_directories(${BINARY_NAME} PRIVATE "${CMAKE_SOURCE_DIR}")

```

### `frontend/linux/runner/main.cc`
`size: 180 bytes`

```cc
#include "my_application.h"

int main(int argc, char** argv) {
  g_autoptr(MyApplication) app = my_application_new();
  return g_application_run(G_APPLICATION(app), argc, argv);
}

```

### `frontend/linux/runner/my_application.cc`
`size: 4750 bytes`

```cc
#include "my_application.h"

#include <flutter_linux/flutter_linux.h>
#ifdef GDK_WINDOWING_X11
#include <gdk/gdkx.h>
#endif

#include "flutter/generated_plugin_registrant.h"

struct _MyApplication {
  GtkApplication parent_instance;
  char** dart_entrypoint_arguments;
};

G_DEFINE_TYPE(MyApplication, my_application, GTK_TYPE_APPLICATION)

// Implements GApplication::activate.
static void my_application_activate(GApplication* application) {
  MyApplication* self = MY_APPLICATION(application);
  GtkWindow* window =
      GTK_WINDOW(gtk_application_window_new(GTK_APPLICATION(application)));

  // Use a header bar when running in GNOME as this is the common style used
  // by applications and is the setup most users will be using (e.g. Ubuntu
  // desktop).
  // If running on X and not using GNOME then just use a traditional title bar
  // in case the window manager does more exotic layout, e.g. tiling.
  // If running on Wayland assume the header bar will work (may need changing
  // if future cases occur).
  gboolean use_header_bar = TRUE;
#ifdef GDK_WINDOWING_X11
  GdkScreen* screen = gtk_window_get_screen(window);
  if (GDK_IS_X11_SCREEN(screen)) {
    const gchar* wm_name = gdk_x11_screen_get_window_manager_name(screen);
    if (g_strcmp0(wm_name, "GNOME Shell") != 0) {
      use_header_bar = FALSE;
    }
  }
#endif
  if (use_header_bar) {
    GtkHeaderBar* header_bar = GTK_HEADER_BAR(gtk_header_bar_new());
    gtk_widget_show(GTK_WIDGET(header_bar));
    gtk_header_bar_set_title(header_bar, "frontend");
    gtk_header_bar_set_show_close_button(header_bar, TRUE);
    gtk_window_set_titlebar(window, GTK_WIDGET(header_bar));
  } else {
    gtk_window_set_title(window, "frontend");
  }

  gtk_window_set_default_size(window, 1280, 720);
  gtk_widget_show(GTK_WIDGET(window));

  g_autoptr(FlDartProject) project = fl_dart_project_new();
  fl_dart_project_set_dart_entrypoint_arguments(project, self->dart_entrypoint_arguments);

  FlView* view = fl_view_new(project);
  gtk_widget_show(GTK_WIDGET(view));
  gtk_container_add(GTK_CONTAINER(window), GTK_WIDGET(view));

  fl_register_plugins(FL_PLUGIN_REGISTRY(view));

  gtk_widget_grab_focus(GTK_WIDGET(view));
}

// Implements GApplication::local_command_line.
static gboolean my_application_local_command_line(GApplication* application, gchar*** arguments, int* exit_status) {
  MyApplication* self = MY_APPLICATION(application);
  // Strip out the first argument as it is the binary name.
  self->dart_entrypoint_arguments = g_strdupv(*arguments + 1);

  g_autoptr(GError) error = nullptr;
  if (!g_application_register(application, nullptr, &error)) {
     g_warning("Failed to register: %s", error->message);
     *exit_status = 1;
     return TRUE;
  }

  g_application_activate(application);
  *exit_status = 0;

  return TRUE;
}

// Implements GApplication::startup.
static void my_application_startup(GApplication* application) {
  //MyApplication* self = MY_APPLICATION(object);

  // Perform any actions required at application startup.

  G_APPLICATION_CLASS(my_application_parent_class)->startup(application);
}

// Implements GApplication::shutdown.
static void my_application_shutdown(GApplication* application) {
  //MyApplication* self = MY_APPLICATION(object);

  // Perform any actions required at application shutdown.

  G_APPLICATION_CLASS(my_application_parent_class)->shutdown(application);
}

// Implements GObject::dispose.
static void my_application_dispose(GObject* object) {
  MyApplication* self = MY_APPLICATION(object);
  g_clear_pointer(&self->dart_entrypoint_arguments, g_strfreev);
  G_OBJECT_CLASS(my_application_parent_class)->dispose(object);
}

static void my_application_class_init(MyApplicationClass* klass) {
  G_APPLICATION_CLASS(klass)->activate = my_application_activate;
  G_APPLICATION_CLASS(klass)->local_command_line = my_application_local_command_line;
  G_APPLICATION_CLASS(klass)->startup = my_application_startup;
  G_APPLICATION_CLASS(klass)->shutdown = my_application_shutdown;
  G_OBJECT_CLASS(klass)->dispose = my_application_dispose;
}

static void my_application_init(MyApplication* self) {}

MyApplication* my_application_new() {
  // Set the program name to the application ID, which helps various systems
  // like GTK and desktop environments map this running application to its
  // corresponding .desktop file. This ensures better integration by allowing
  // the application to be recognized beyond its binary name.
  g_set_prgname(APPLICATION_ID);

  return MY_APPLICATION(g_object_new(my_application_get_type(),
                                     "application-id", APPLICATION_ID,
                                     "flags", G_APPLICATION_NON_UNIQUE,
                                     nullptr));
}

```

### `frontend/linux/runner/my_application.h`
`size: 388 bytes`

```h
#ifndef FLUTTER_MY_APPLICATION_H_
#define FLUTTER_MY_APPLICATION_H_

#include <gtk/gtk.h>

G_DECLARE_FINAL_TYPE(MyApplication, my_application, MY, APPLICATION,
                     GtkApplication)

/**
 * my_application_new:
 *
 * Creates a new Flutter-based application.
 *
 * Returns: a new #MyApplication.
 */
MyApplication* my_application_new();

#endif  // FLUTTER_MY_APPLICATION_H_

```

### `frontend/linux/flutter/CMakeLists.txt`
`size: 2815 bytes`

```txt
# This file controls Flutter-level build steps. It should not be edited.
cmake_minimum_required(VERSION 3.10)

set(EPHEMERAL_DIR "${CMAKE_CURRENT_SOURCE_DIR}/ephemeral")

# Configuration provided via flutter tool.
include(${EPHEMERAL_DIR}/generated_config.cmake)

# TODO: Move the rest of this into files in ephemeral. See
# https://github.com/flutter/flutter/issues/57146.

# Serves the same purpose as list(TRANSFORM ... PREPEND ...),
# which isn't available in 3.10.
function(list_prepend LIST_NAME PREFIX)
    set(NEW_LIST "")
    foreach(element ${${LIST_NAME}})
        list(APPEND NEW_LIST "${PREFIX}${element}")
    endforeach(element)
    set(${LIST_NAME} "${NEW_LIST}" PARENT_SCOPE)
endfunction()

# === Flutter Library ===
# System-level dependencies.
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK REQUIRED IMPORTED_TARGET gtk+-3.0)
pkg_check_modules(GLIB REQUIRED IMPORTED_TARGET glib-2.0)
pkg_check_modules(GIO REQUIRED IMPORTED_TARGET gio-2.0)

set(FLUTTER_LIBRARY "${EPHEMERAL_DIR}/libflutter_linux_gtk.so")

# Published to parent scope for install step.
set(FLUTTER_LIBRARY ${FLUTTER_LIBRARY} PARENT_SCOPE)
set(FLUTTER_ICU_DATA_FILE "${EPHEMERAL_DIR}/icudtl.dat" PARENT_SCOPE)
set(PROJECT_BUILD_DIR "${PROJECT_DIR}/build/" PARENT_SCOPE)
set(AOT_LIBRARY "${PROJECT_DIR}/build/lib/libapp.so" PARENT_SCOPE)

list(APPEND FLUTTER_LIBRARY_HEADERS
  "fl_basic_message_channel.h"
  "fl_binary_codec.h"
  "fl_binary_messenger.h"
  "fl_dart_project.h"
  "fl_engine.h"
  "fl_json_message_codec.h"
  "fl_json_method_codec.h"
  "fl_message_codec.h"
  "fl_method_call.h"
  "fl_method_channel.h"
  "fl_method_codec.h"
  "fl_method_response.h"
  "fl_plugin_registrar.h"
  "fl_plugin_registry.h"
  "fl_standard_message_codec.h"
  "fl_standard_method_codec.h"
  "fl_string_codec.h"
  "fl_value.h"
  "fl_view.h"
  "flutter_linux.h"
)
list_prepend(FLUTTER_LIBRARY_HEADERS "${EPHEMERAL_DIR}/flutter_linux/")
add_library(flutter INTERFACE)
target_include_directories(flutter INTERFACE
  "${EPHEMERAL_DIR}"
)
target_link_libraries(flutter INTERFACE "${FLUTTER_LIBRARY}")
target_link_libraries(flutter INTERFACE
  PkgConfig::GTK
  PkgConfig::GLIB
  PkgConfig::GIO
)
add_dependencies(flutter flutter_assemble)

# === Flutter tool backend ===
# _phony_ is a non-existent file to force this command to run every time,
# since currently there's no way to get a full input/output list from the
# flutter tool.
add_custom_command(
  OUTPUT ${FLUTTER_LIBRARY} ${FLUTTER_LIBRARY_HEADERS}
    ${CMAKE_CURRENT_BINARY_DIR}/_phony_
  COMMAND ${CMAKE_COMMAND} -E env
    ${FLUTTER_TOOL_ENVIRONMENT}
    "${FLUTTER_ROOT}/packages/flutter_tools/bin/tool_backend.sh"
      ${FLUTTER_TARGET_PLATFORM} ${CMAKE_BUILD_TYPE}
  VERBATIM
)
add_custom_target(flutter_assemble DEPENDS
  "${FLUTTER_LIBRARY}"
  ${FLUTTER_LIBRARY_HEADERS}
)

```

### `frontend/linux/flutter/generated_plugin_registrant.cc`
`size: 161 bytes`

```cc
//
//  Generated file. Do not edit.
//

// clang-format off

#include "generated_plugin_registrant.h"


void fl_register_plugins(FlPluginRegistry* registry) {
}

```

### `frontend/linux/flutter/generated_plugin_registrant.h`
`size: 303 bytes`

```h
//
//  Generated file. Do not edit.
//

// clang-format off

#ifndef GENERATED_PLUGIN_REGISTRANT_
#define GENERATED_PLUGIN_REGISTRANT_

#include <flutter_linux/flutter_linux.h>

// Registers Flutter plugins.
void fl_register_plugins(FlPluginRegistry* registry);

#endif  // GENERATED_PLUGIN_REGISTRANT_

```

### `frontend/linux/flutter/generated_plugins.cmake`
`size: 739 bytes`

```cmake
#
# Generated file, do not edit.
#

list(APPEND FLUTTER_PLUGIN_LIST
)

list(APPEND FLUTTER_FFI_PLUGIN_LIST
)

set(PLUGIN_BUNDLED_LIBRARIES)

foreach(plugin ${FLUTTER_PLUGIN_LIST})
  add_subdirectory(flutter/ephemeral/.plugin_symlinks/${plugin}/linux plugins/${plugin})
  target_link_libraries(${BINARY_NAME} PRIVATE ${plugin}_plugin)
  list(APPEND PLUGIN_BUNDLED_LIBRARIES $<TARGET_FILE:${plugin}_plugin>)
  list(APPEND PLUGIN_BUNDLED_LIBRARIES ${${plugin}_bundled_libraries})
endforeach(plugin)

foreach(ffi_plugin ${FLUTTER_FFI_PLUGIN_LIST})
  add_subdirectory(flutter/ephemeral/.plugin_symlinks/${ffi_plugin}/linux plugins/${ffi_plugin})
  list(APPEND PLUGIN_BUNDLED_LIBRARIES ${${ffi_plugin}_bundled_libraries})
endforeach(ffi_plugin)

```

### `.github/workflows/make_gpt_bundle.yml`
`size: 5854 bytes`

```yml
name: Make GPT Bundle

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:
permissions:
  contents: write

jobs:
  bundle:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      # 1) 번들러 스크립트를 레포 내부에 생성
      - name: Create bundler script
        run: |
          mkdir -p .github/tools
          cat > .github/tools/gpt_repo_bundler.py << 'PY'
          #!/usr/bin/env python3
          import argparse, os
          from pathlib import Path
          from datetime import datetime

          DEFAULT_INCLUDE = ["backend", "frontend", ".github", "README.md"]
          DEFAULT_EXCLUDE = [
              ".git",".github/workflows","venv",".venv","node_modules","build",".dart_tool","__pycache__",
              "*.env","*.pkl","*.pt","*.onnx","*.h5","*.bin","*.dll","*.so",
              "*.zip","*.7z","*.rar","*.tar","*.gz","*.xz","*.png","*.jpg","*.jpeg","*.gif","*.webp","*.pdf"
          ]
          TEXT_EXTS = {".py",".dart",".yaml",".yml",".json",".md",".txt",".js",".ts",".html",".css",".toml",".ini",".cfg",".sql"}

          def matches_any(p, pats):
              from pathlib import Path as _P
              for pat in pats:
                  if "*" in pat or "?" in pat:
                      if _P(p).match(pat): return True
                  else:
                      if pat in p.split(os.sep): return True
              return False

          def short_tree(root, include, exclude):
              lines=[]
              for dp, dns, fns in os.walk(root):
                  rel = Path(dp).relative_to(root) if Path(dp)!=root else Path(".")
                  dns[:] = [d for d in dns if not matches_any(str((rel/ d)), exclude)]
                  rels = str(rel).replace("\\","/")
                  if include and rels!="." and not any(rels.startswith(i.strip("/")) for i in include): 
                      continue
                  lines.append(str(rel))
                  for f in sorted(fns):
                      p=str(rel / f)
                      if matches_any(p, exclude): continue
                      lines.append("  "+p)
              return "\n".join(lines)

          def is_text(path:Path):
              if path.suffix.lower() in TEXT_EXTS: return True
              try:
                  b=open(path,"rb").read(4096)
                  if b"\x00" in b: return False
                  b.decode("utf-8")
                  return True
              except: return False

          def main():
              ap=argparse.ArgumentParser()
              ap.add_argument("--out", default="gpt_bundle.md")
              ap.add_argument("--include", nargs="*", default=DEFAULT_INCLUDE)
              ap.add_argument("--exclude", nargs="*", default=DEFAULT_EXCLUDE)
              ap.add_argument("--max-bytes", type=int, default=200_000)
              ap.add_argument("--max-files", type=int, default=400)
              args=ap.parse_args()

              root=Path(".").resolve()
              out=Path(args.out).resolve()
              with open(out,"w",encoding="utf-8") as fp:
                  fp.write(f"# GPT Bundle — TempAI-public\n")
                  fp.write(f"- Generated: {datetime.utcnow().isoformat()}Z\n\n")
                  fp.write("## Directory tree (filtered)\n\n```\n")
                  fp.write(short_tree(root,[p.replace('\\','/').strip('/') for p in args.include],args.exclude))
                  fp.write("\n```\n\n## Files (truncated)\n")

                  count=0
                  for dp,dns,fns in os.walk(root):
                      rel=Path(dp).relative_to(root)
                      dns[:]=[d for d in dns if not matches_any(str((rel/d)).replace("\\","/"), args.exclude)]
                      rels=str(rel).replace("\\","/")
                      if args.include and rels!="." and not any(rels.startswith(i.strip('/')) for i in args.include):
                          continue
                      for f in sorted(fns):
                          relf=Path(rel,f); relsfile=str(relf).replace("\\","/")
                          p=Path(dp)/f
                          if matches_any(relsfile,args.exclude): continue
                          if not is_text(p): continue
                          size=p.stat().st_size
                          if count>=args.max_files:
                              fp.write("\n> **File limit reached.**\n"); break
                          content=open(p,"r",encoding="utf-8",errors="replace").read(args.max_bytes+1)
                          trunc = len(content)>args.max_bytes
                          if trunc: content=content[:args.max_bytes]
                          fp.write(f"\n### `{relsfile}`\n`size: {size} bytes`")
                          if trunc: fp.write(f" — *(truncated to {args.max_bytes} bytes)*")
                          fp.write("\n\n```{}\n".format(p.suffix.lstrip('.') or ''))
                          fp.write(content); fp.write("\n```\n")
                          count+=1
                  fp.write(f"\n---\n_Total embedded files: {count}_\n")

          if __name__=="__main__": main()
          PY

      # 2) 번들 생성
      - name: Run bundler
        run: |
          python .github/tools/gpt_repo_bundler.py \
            --out gpt_bundle.md \
            --include backend frontend .github README.md \
            --max-bytes 200000

      # 3) 무조건 커밋/푸시 (변경 없어도 시도)
      - name: Commit bundle
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add gpt_bundle.md
          git commit -m "docs: update gpt_bundle.md" || echo "No changes to commit"
          git push

```

### `.github/tools/gpt_repo_bundler.py`
`size: 3859 bytes`

```py
#!/usr/bin/env python3
import argparse, os
from pathlib import Path
from datetime import datetime

DEFAULT_INCLUDE = ["backend", "frontend", ".github", "README.md"]
DEFAULT_EXCLUDE = [
    ".git",".github/workflows","venv",".venv","node_modules","build",".dart_tool","__pycache__",
    "*.env","*.pkl","*.pt","*.onnx","*.h5","*.bin","*.dll","*.so",
    "*.zip","*.7z","*.rar","*.tar","*.gz","*.xz","*.png","*.jpg","*.jpeg","*.gif","*.webp","*.pdf"
]
TEXT_EXTS = {".py",".dart",".yaml",".yml",".json",".md",".txt",".js",".ts",".html",".css",".toml",".ini",".cfg",".sql"}

def matches_any(p, pats):
    from pathlib import Path as _P
    for pat in pats:
        if "*" in pat or "?" in pat:
            if _P(p).match(pat): return True
        else:
            if pat in p.split(os.sep): return True
    return False

def short_tree(root, include, exclude):
    lines=[]
    for dp, dns, fns in os.walk(root):
        rel = Path(dp).relative_to(root) if Path(dp)!=root else Path(".")
        dns[:] = [d for d in dns if not matches_any(str((rel/ d)), exclude)]
        rels = str(rel).replace("\\","/")
        if include and rels!="." and not any(rels.startswith(i.strip("/")) for i in include): 
            continue
        lines.append(str(rel))
        for f in sorted(fns):
            p=str(rel / f)
            if matches_any(p, exclude): continue
            lines.append("  "+p)
    return "\n".join(lines)

def is_text(path:Path):
    if path.suffix.lower() in TEXT_EXTS: return True
    try:
        b=open(path,"rb").read(4096)
        if b"\x00" in b: return False
        b.decode("utf-8")
        return True
    except: return False

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out", default="gpt_bundle.md")
    ap.add_argument("--include", nargs="*", default=DEFAULT_INCLUDE)
    ap.add_argument("--exclude", nargs="*", default=DEFAULT_EXCLUDE)
    ap.add_argument("--max-bytes", type=int, default=200_000)
    ap.add_argument("--max-files", type=int, default=400)
    args=ap.parse_args()

    root=Path(".").resolve()
    out=Path(args.out).resolve()
    with open(out,"w",encoding="utf-8") as fp:
        fp.write(f"# GPT Bundle — TempAI-public\n")
        fp.write(f"- Generated: {datetime.utcnow().isoformat()}Z\n\n")
        fp.write("## Directory tree (filtered)\n\n```\n")
        fp.write(short_tree(root,[p.replace('\\','/').strip('/') for p in args.include],args.exclude))
        fp.write("\n```\n\n## Files (truncated)\n")

        count=0
        for dp,dns,fns in os.walk(root):
            rel=Path(dp).relative_to(root)
            dns[:]=[d for d in dns if not matches_any(str((rel/d)).replace("\\","/"), args.exclude)]
            rels=str(rel).replace("\\","/")
            if args.include and rels!="." and not any(rels.startswith(i.strip('/')) for i in args.include):
                continue
            for f in sorted(fns):
                relf=Path(rel,f); relsfile=str(relf).replace("\\","/")
                p=Path(dp)/f
                if matches_any(relsfile,args.exclude): continue
                if not is_text(p): continue
                size=p.stat().st_size
                if count>=args.max_files:
                    fp.write("\n> **File limit reached.**\n"); break
                content=open(p,"r",encoding="utf-8",errors="replace").read(args.max_bytes+1)
                trunc = len(content)>args.max_bytes
                if trunc: content=content[:args.max_bytes]
                fp.write(f"\n### `{relsfile}`\n`size: {size} bytes`")
                if trunc: fp.write(f" — *(truncated to {args.max_bytes} bytes)*")
                fp.write("\n\n```{}\n".format(p.suffix.lstrip('.') or ''))
                fp.write(content); fp.write("\n```\n")
                count+=1
        fp.write(f"\n---\n_Total embedded files: {count}_\n")

if __name__=="__main__": main()

```

---
_Total embedded files: 122_
