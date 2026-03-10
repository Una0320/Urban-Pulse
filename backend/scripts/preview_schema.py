"""
檔案作用說明：針對一般資料格式進行欄位結構分析 (Schema Analysis)，檢查資料型別、缺失值比例與數據分佈，產出簡易體檢報告。
包含的 Function / Class：
    - analyze_data_structure (Function)
"""

import pandas as pd
import os

def analyze_data_structure(file_path="data/processed/Taipei_bus_shapes.parquet"):
    if not os.path.exists(file_path):
        print(f"❌ 找不到檔案: {file_path}")
        return

    df = pd.read_parquet(file_path)
    
    print("\n" + "🚀" + "="*40)
    print(f" 數據結構體檢報告: {os.path.basename(file_path)}")
    print("="*41)
    
    # 1. 規模統計
    print(f"\n[ 1. 基本規模 ]")
    print(f"總資料筆數: {len(df):,}")
    print(f"總欄位數量: {len(df.columns)}")
    
    # 2. 欄位型別與缺失值 (Null) 檢查
    print(f"\n[ 2. 欄位明細與品質 ]")
    info_df = pd.DataFrame({
        "資料型別": df.dtypes,
        "非空值筆數": df.count(),
        "缺失值比例(%)": (df.isnull().sum() / len(df) * 100).round(2)
    })
    print(info_df)
    
    # 3. 數據內容預覽
    print(f"\n[ 3. 前 5 筆資料範例 ]")
    # 使用 to_string 確保在 terminal 裡排版整齊
    print(df.head(5).to_string())

if __name__ == "__main__":
    analyze_data_structure()