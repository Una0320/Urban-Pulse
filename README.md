# Urban-Pulse
建立前後端DevOps完整流程，以都市數據為主

## 🏗 專案架構 (Directory Structure)

```text
Urban-Pulse/
├── backend/                # FastAPI 後端與 ETL 流程
│   ├── app/                # 核心應用程式邏輯
│   │   ├── api/            # 路由層 (Routers)：負責 HTTP 請求收發與參數驗證
│   │   ├── core/           # 核心層 (Core)：系統全局配置、資料庫初始化與安全認證
│   │   ├── services/       # 服務層 (Services)：封裝 TDX 串接、數據清洗與 Parquet 轉換
│   │   └── models/         # 模型層 (Models)：MongoDB Schema 與 Pydantic 資料結構
│   ├── data/               # 數據存放 (受 .gitignore 保護)
│   │   ├── raw/            # 原始 JSON 快照
│   │   └── processed/      # 經過清洗與壓縮的 Parquet 檔案
│   ├── .env.example        # 環境變數範本
│   ├── run_etl.py          # 數據任務執行進入點
│   └── requirements.txt    # Python 依賴清單 (pip freeze 產出)
├── frontend/               # React 前端 (Vercel)
├── CodingStyle.md          # 團隊開發與命名規範
└── README.md
```

## 🚀 開發指令 (Development)

### 1. 環境設定
- 建立虛擬環境: `python -m venv venv`
- 啟動環境: `source venv/bin/activate` (Mac/Linux) 或 `.\venv\Scripts\activate` (Windows)
- 安裝套件: `pip install -r requirements.txt`

### 2. 數據抓取與處理 (ETL)
統一的進入點來執行數據任務(fetch, process..)：
- **執行全量抓取**: `python run_etl.py`

### 3. 後端伺服器啟動
- `uvicorn app.main:app --reload` (稍後實作)