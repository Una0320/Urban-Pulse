from app.core.config import settings
import time
import requests
import json
import os

class TdxService:
    def __init__(self, token_cache_path="token.json"):
        # 直接從 settings 拿，不需要再管 os.getenv 或 load_dotenv()
        self.client_id = settings.TDX_CLIENT_ID
        self.client_secret = settings.TDX_CLIENT_SECRET
        
        self.cache_path = token_cache_path
        self.access_token = None
        self.token_expires_at = 0
        self._load_token_from_disk()

    def _load_token_from_disk(self):
        """從本地 JSON 讀取 Token"""
        if os.path.exists(self.cache_path):
            try:
                with open(self.cache_path, 'r') as f:
                    data = json.load(f)
                    self.access_token = data.get('token')
                    self.token_expires_at = data.get('expires_at', 0)
                    print("從本地 JSON 載入 Token 成功")
            except Exception as e:
                print(f"載入 JSON 失敗: {e}")

    def _save_token_to_disk(self):
        """將 Token 存入本地 JSON"""
        try:
            with open(self.cache_path, 'w') as f:
                json.dump({
                    "token": self.access_token,
                    "expires_at": self.token_expires_at
                }, f)
        except Exception as e:
            print(f"儲存 JSON 失敗: {e}")

    def _get_new_token(self):
        auth_url = "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
        payload = {
            'content-type': 'application/x-www-form-urlencoded',
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        
        response = requests.post(auth_url, data=payload)
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get('access_token')
            self.token_expires_at = time.time() + data.get('expires_in', 3600) - 60
            
            # 更新後存入硬碟
            self._save_token_to_disk()
            return self.access_token
        else:
            raise Exception(f"無法取得 TDX Token: {response.text}")

    def get_token(self):
        # 檢查記憶體中的 Token 是否過期
        if not self.access_token or time.time() > self.token_expires_at:
            print("Token 已過期或不存在，向 TDX 請求新 Token...")
            return self._get_new_token()
        return self.access_token

    def get_auth_header(self):
        return {
            'authorization': f'Bearer {self.get_token()}',
            'Accept-Encoding': 'gzip'
        }

if __name__ == "__main__":
    tdx = TdxService()
    print(f"Token: {tdx.get_token()[:20]}...")