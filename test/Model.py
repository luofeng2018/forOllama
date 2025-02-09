import requests
import os

class Model:
    def __init__(self, api_url=None):
        self.api_url = api_url or os.getenv("GLM_API_URL", "http://127.0.0.1:11434/api/generate")

    def ask_glm(self, content):
        data = {
            "model": "deepseek-r1:latest",
            "prompt": content,
            "stream": False
        }

        try:
            response = requests.post(self.api_url, json=data)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"请求失败，状态码：{response.status_code}, 响应内容：{response.text}")
        except Exception as e:
            print(f"请求大模型API时发生错误：{e}")
        return None
