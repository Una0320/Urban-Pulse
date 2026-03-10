"""
檔案作用說明：驗證 Python 環境是否能成功連線至 Docker 容器內運行的 MongoDB 服務。
包含的 Function / Class：
- test_connection (Async Function)

執行指令 (請在 backend/ 目錄下執行)：
python -m scripts.test_db
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# 設定連線字串 (對應 Docker -p 27017:27017 設定)
MONGODB_URI = "mongodb://localhost:27017"

async def test_connection():
    """
    執行非同步連線測試，並列出當前資料庫清單。
    """
    print(f"--- 🔌 啟動 MongoDB 連線測試: {MONGODB_URI} ---")
    try:
        # 1. 初始化 Client
        client = AsyncIOMotorClient(MONGODB_URI)
        
        # 2. 嘗試 Ping 資料庫 (發送一個極小的管理指令確認反應)
        await client.admin.command('ping')
        print("✅ 連線成功！MongoDB Docker版 已就緒。")
        
        # 3. 獲取當前所有資料庫名稱，確認權限與狀態
        dbs = await client.list_database_names()
        print(f"📂 目前系統內的資料庫清單: {dbs}")
        
    except Exception as e:
        print(f"❌ 連線失敗，請檢查 Docker 容器是否正在運行。")
        print(f"詳細錯誤訊息: {e}")

if __name__ == "__main__":
    # 使用 asyncio 驅動非同步主程式
    asyncio.run(test_connection())