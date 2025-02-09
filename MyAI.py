import os

import gradio as gr
import requests


# 定义与模型交互的函数
def ask_glm(content):
    url = os.getenv("GLM_API_URL", "http://127.0.0.1:11434/api/generate")
    # deepseek-r1:latest ，qwen2:1.5b
    data = {
        "model": "deepseek-r1:latest",
        "prompt": content,  # 确保将用户的问题传递给大模型
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            print(f"请求失败，状态码：{response.status_code}, 响应内容：{response.text}")
    except Exception as e:
        print(f"请求大模型API时发生错误：{e}")
    return None

# 创建Gradio界面
def gradio_interface(user_question):
    # 获取模型的回答
    answer = ask_glm(user_question)
    if answer and 'response' in answer:
        message_content = answer.get('response', '')
        if not message_content:
            message_content = '无法回答问题'
    else:
        message_content = '无法获取答案，请稍后重试。'

    # 返回模型的回答
    return message_content

# 创建 Gradio 界面
iface = gr.Interface(
    fn=gradio_interface,  # 绑定上面的函数
    inputs=gr.Textbox(label="请输入你的问题：", placeholder="在这里输入问题", lines=2),  # 用户输入框
    outputs=gr.Textbox(label="模型的回答："),  # 模型回答框
    title="My AI",  # 设置网页标题
    description="My AI",  # 描述
)

# 启动 Gradio 界面
iface.launch()
