import gradio as gr

class View:
    def __init__(self, controller):
        self.controller = controller

    def gradio_interface(self, user_question):
        return self.controller.process_user_question(user_question)

    def launch(self):
        iface = gr.Interface(
            fn=self.gradio_interface,  # 绑定控制器的接口函数
            inputs=gr.Textbox(label="请输入你的问题：", placeholder="在这里输入问题", lines=2),  # 用户输入框
            outputs=gr.Textbox(label="模型的回答："),  # 模型回答框
            title="MyAI",  # 设置网页标题
            description="AI for local",  # 描述
        )

        # 启动 Gradio 界面
        iface.launch()
