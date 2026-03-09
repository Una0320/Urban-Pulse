from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# 定義專案根目錄 (Urban-Pulse/backend)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    # 專案基本資訊
    PROJECT_NAME: str = "Urban-Pulse API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # TDX 憑證 (會自動對應 .env 裡的 key)
    TDX_CLIENT_ID: str
    TDX_CLIENT_SECRET: str

    # 資料庫設定
    MONGODB_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "urban_pulse"

    # 強制 Pydantic 去讀取 .env 檔案
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", 
        env_file_encoding='utf-8',
        extra='ignore' # 忽略 .env 中多餘的變數
    )

# 實例化，全專案共用這一個 settings 物件
settings = Settings()