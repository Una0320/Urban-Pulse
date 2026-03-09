import os
import requests
import pandas as pd
import json
from app.services.tdx_service import TdxService

def fetch_and_save_geometries(city="Taipei"):
    # 1. 初始化 TDX 服務
    tdx = TdxService()
    
    # 2. 定義 API URL (我們先抓前 100 筆測試，之後可以去掉 $top)
    # 這裡抓的是公車線型 (Shape) 資料
    url = f"https://tdx.transportdata.tw/api/basic/v2/Bus/Shape/City/{city}?$top=100&$format=JSON"
    
    print(f"--- 開始抓取 {city} 公車路網資料 ---")
    
    try:
        response = requests.get(url, headers=tdx.get_auth_header())
        response.raise_for_status() # 如果狀態碼不是 200 會拋出錯誤
        data = response.json()
        
        # 3. 確保資料夾存在
        raw_dir = "data/raw"
        processed_dir = "data/processed"
        os.makedirs(raw_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)

        # 4. 存成原始 JSON (備份用)
        raw_path = os.path.join(raw_dir, f"{city}_bus_shapes.json")
        with open(raw_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        print(f"已儲存原始 JSON: {raw_path}")

        # 5. 資料清洗與轉換 (Pandas)
        df = pd.DataFrame(data)
        
        # 觀察欄位，通常我們只需要：RouteID, RouteName, Geometry
        # TDX 的 Geometry 欄位通常是 WKT 格式或座標字串
        # 這裡我們示範只取核心欄位
        important_columns = ['RouteID', 'RouteName', 'Geometry', 'UpdateTime']
        # 檢查欄位是否存在，避免噴錯
        df = df[[col for col in important_columns if col in df.columns]]

        # 6. 存成 Parquet (高效能格式)
        processed_path = os.path.join(processed_dir, f"{city}_bus_shapes.parquet")
        df.to_parquet(processed_path, engine='pyarrow', index=False)
        
        print(f"成功轉換為 Parquet: {processed_path}")
        print(f"資料筆數: {len(df)}")

    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    fetch_and_save_geometries()