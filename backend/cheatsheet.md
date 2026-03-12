# 🚀 Urban-Pulse 後端指令工具箱

這份文件記錄了後端開發過程中常用的指令，避免因遺忘而導致開發中斷。

---

## 🐳 Docker 基礎設施
用於管理 MongoDB 資料庫環境。

- **啟動全新容器 (僅第一次執行)**:
  `docker run -d --name urban-pulse-mongo -p 27017:27017 mongo`
- **停止資料庫**:
  `docker stop urban-pulse-mongo`
- **再次喚醒資料庫 (隔天啟動用)**:
  `docker start urban-pulse-mongo`

---

## 🐍 Python 環境管理
- **啟動虛擬環境 (Venv)**:
  `source venv/bin/activate`
- **安裝必要套件**:
  `pip install -r requirements.txt`
- **更新套件清單**:
  `pip freeze > requirements.txt`

---

## 🛠️ 數據與驗證腳本 (Scripts)
*注意：請在 `backend/` 目錄下執行，並確保已啟動 venv。*

- **資料庫連線測試**:
  `python -m scripts.test_db`
- **地理圖資預覽 (座標校正)**:
  `python -m scripts.preview_map`
- **數據結構分析 (Schema QA)**:
  `python -m scripts.preview_schema`

---

## ⚙️ 核心流程啟動
- **執行 ETL 數據任務 (抓取/轉換/存檔)**:
  `python run_etl.py`
- **啟動 FastAPI 伺服器 (開發模式)**:
  `uvicorn app.main:app --reload`
  - 首頁測試：`http://127.0.0.1:8000/`
  - 日誌查看：`http://127.0.0.1:8000/logs`

---

## 💾 Git 常用提交類型
- `feat(module):` 新增功能
- `refactor(module):` 重構程式碼
- `docs(module):` 文件更動 (如：更新此 cheatsheet)
- `fix(module):` 修復 Bug