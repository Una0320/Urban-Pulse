"""
檔案作用說明：專案的數據任務執行進入點 (Entry Point)，負責主動調用各項 ETL (擷取、轉換、負載) 邏輯。
包含的 Function / Class：
- main (Async Function): 協調各項數據抓取任務的執行順序。

執行指令 (請在 backend/ 目錄下執行)：
python run_etl.py
"""

import asyncio
# 確保這裡的 import 路徑是你目前的檔名 (fetch_bus_geometries 或 fetch_tdx_bus_geometries)
from app.services.fetch_tdx_bus_geometries import fetch_and_save_geometries

async def main():
    print("🚀 [Urban-Pulse ETL] 啟動自動化數據任務...")
    
    # 執行公車幾何資料抓取
    await fetch_and_save_geometries(city="Taipei")
    
    # 未來可擴充其他城市或類型的任務
    # await fetch_bus_stops(city="Taipei")

    print("🏁 [Urban-Pulse ETL] 所有數據任務已完成。")

if __name__ == "__main__":
    # 使用 asyncio 啟動最高層級的協程
    asyncio.run(main())