"""
檔案作用說明：讀取處理後的 Parquet 檔案，並利用 GeoPandas 進行經緯度座標校正預覽，確保地圖圖資未發生偏移或損壞。
包含的 Function / Class：
    - preview_map_shapes (Function)
"""

import pandas as pd
import geopandas as gpd
from shapely import wkt
import matplotlib.pyplot as plt
import os

def preview_map_shapes(file_path="data/processed/Taipei_bus_shapes.parquet"):
    if not os.path.exists(file_path):
        print(f"❌ 找不到檔案: {file_path}，請先執行 run_etl.py")
        return

    print(f"--- 🗺️ 啟動地理資訊預覽: {file_path} ---")
    
    # 讀取數據
    df = pd.read_parquet(file_path)
    
    # 將 WKT (Well-Known Text) 轉為幾何對象
    print("正在解析 WKT 座標系統...")
    df['geometry'] = df['Geometry'].apply(wkt.loads)
    
    # 建立 GeoDataFrame (指定 WGS84 座標系)
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
    
    # 繪圖設定
    print("正在繪製地圖輪廓...")
    fig, ax = plt.subplots(figsize=(12, 10))
    gdf.plot(ax=ax, linewidth=0.6, color='#3498db', alpha=0.6)
    
    ax.set_title(f"Bus Route Spatial Preview\n{file_path}", fontsize=14)
    ax.set_xlabel("Longitude (經度)")
    ax.set_ylabel("Latitude (緯度)")
    ax.grid(True, linestyle=':', alpha=0.6)
    
    print("✅ 預覽視窗已開啟，請檢查座標範圍是否落在 121.5, 25.0 附近（台北市）。")
    plt.show()

if __name__ == "__main__":
    # 啟動預覽
    preview_map_shapes()