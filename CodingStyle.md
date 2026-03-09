# Coding Style

## 1. 命名規範
- **資料夾 (Directories)**: 全小寫並使用橫線分隔 `kebab-case` (e.g., `data-processor`)。
- **Python 檔案 (Scripts)**: 全小寫並使用底線分隔 `snake_case` (e.g., `fetch_tdx.py`)。
- **React 組件**: 大駝峰 `PascalCase` (e.g., `MapLayer.tsx`)。
- **變數/函式 (JS/TS)**: 小駝峰 `camelCase` (e.g., `fetchData()`)。
- **環境變數 (.env)**: 全大寫並使用底線 `SCREAMING_SNAKE_CASE` (e.g., `TDX_CLIENT_ID`)。

## 2. Git 規範
- **提交格式**: `類型(模組): 描述` (可中文描述)。
- **常用類型**:
  - `feat`: 新功能
  - `fix`: 修復 Bug
  - `docs`: 文件更動
  - `style`: 格式調整 (不影響邏輯)
  - `refactor`: 重構代碼
  - `chore`: 工具/環境變動 (e.g., 更新 .gitignore)

## 3. 前端架構
- 全域狀態管理 (Zustand/Redux) 需獨立存放於 `src/zustand/` 或 `src/redux/` 資料夾，與一般 Hooks 區分。

## 4. 數據安全
- 嚴禁將 API Keys、Tokens 或超過 5MB 的數據檔案提交至 GitHub。
- 大型數據請放置於 `backend/data/` 並確保在 `.gitignore` 名單內。