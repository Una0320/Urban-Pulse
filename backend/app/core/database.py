from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging

# 1. 初始化 Client
# Motor 是非同步驅動，適合 FastAPI 的高效能需求
client = AsyncIOMotorClient(settings.MONGODB_URI)

# 2. 指定資料庫名稱
db = client[settings.DATABASE_NAME]

async def check_db_connection():
    """
    檢查資料庫連線狀態
    這可以用在系統啟動時的自我檢測 (Health Check)
    """
    try:
        # 發送 admin 指令 ping 資料庫
        await client.admin.command('ping')
        print("✅ MongoDB 連線成功！")
        return True
    except Exception as e:
        logging.error(f"❌ MongoDB 連線失敗: {e}")
        return False