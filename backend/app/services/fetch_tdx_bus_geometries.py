"""
檔案作用說明：負責從交通數據來源抓取公車路網幾何資料，進行清洗後存儲為 Parquet 格式，並記錄任務狀態至 MongoDB。
包含的 Function / Class：
    - fetch_and_save_geometries (Function)
"""
import os
import requests
import pandas as pd
import json
from app.services.tdx_service import TdxService
from app.core.database import db
from app.models.task import TaskLog
import asyncio

async def fetch_and_save_geometries(city="Taipei"):
    tdx = TdxService()
    url = f"https://tdx.transportdata.tw/api/basic/v2/Bus/Shape/City/{city}?$top=100&$format=JSON"
    
    print(f"--- 開始抓取 {city} 公車路網資料 ---")
    
    status = "success"
    error_msg = None
    count = 0
    processed_path = ""

    try:
        response = requests.get(url, headers=tdx.get_auth_header())
        response.raise_for_status()
        data = response.json()
        count = len(data)

        # 建立資料夾
        os.makedirs("data/raw", exist_ok=True)
        os.makedirs("data/processed", exist_ok=True)

        # 轉換與存檔
        df = pd.DataFrame(data)
        processed_path = f"data/processed/{city}_bus_shapes.parquet"
        df.to_parquet(processed_path, engine='pyarrow', index=False)
        print(f"✅ 成功轉換 Parquet: {processed_path}")

    except Exception as e:
        status = "failed"
        error_msg = str(e)
        print(f"❌ 發生錯誤: {e}")

    # --- 重點：將任務結果存入 MongoDB ---
    task_data = TaskLog(
        task_name="fetch_bus_shapes",
        city=city,
        status=status,
        records_count=count,
        file_path=processed_path,
        error_message=error_msg
    )
    
    # 存入名為 "TaskLogs" 的 Collection（MongoDB 的特性是 "On-demand"，第一次對一個不存在的 Collection 寫入資料時，它會自動建立）
    await db.TaskLogs.insert_one(task_data.model_dump())
    print("📝 任務紀錄已寫入 MongoDB")

if __name__ == "__main__":
    # 因為現在有 async 操作，執行方式要微調
    asyncio.run(fetch_and_save_geometries())