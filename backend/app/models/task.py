from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskLog(BaseModel):
    task_name: str                  # 任務名稱，例如 "fetch_bus_shapes"
    city: str                       # 城市，例如 "Taipei"
    status: str                     # 狀態: "success" 或 "failed"
    records_count: int              # 抓到的資料筆數
    file_path: str                  # 存檔路徑
    error_message: Optional[str] = None # 如果失敗，紀錄錯誤訊息
    created_at: datetime = Field(default_factory=datetime.now) # 自動產生時間