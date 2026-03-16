"""
檔案作用說明：FastAPI 應用程式的主進入點，負責初始化伺服器、掛載路由與管理生命週期。
包含的 Function / Class：
- app (FastAPI Instance)
- root (Async Function)
- get_task_logs (Async Function)
"""

from fastapi import FastAPI
from app.core.database import db
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

# 初始化 FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# --- CORS 設定開始 ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # 允許的來源
    allow_credentials=True,
    allow_methods=["*"],         # 允許所有方法 (GET, POST 等)
    allow_headers=["*"],         # 允許所有 Header
)
# --- CORS 設定結束 ---

@app.get("/")
async def root():
    """首頁測試接口"""
    return {
        "project": settings.PROJECT_NAME,
        "status": "online",
        "message": "Welcome to Urban-Pulse API"
    }

@app.get("/logs")
async def get_task_logs():
    """
    從 MongoDB 的 TaskLog Collection 抓取最後 10 筆任務紀錄
    """
    cursor = db.TaskLogs.find().sort("created_at", -1).limit(10)
    logs = []
    
    async for doc in cursor:
        # MongoDB 的 _id 是 ObjectId 物件，必須轉成字串才能變 JSON 回傳
        doc["_id"] = str(doc["_id"])
        logs.append(doc)
    
    return {"count": len(logs), "data": logs}