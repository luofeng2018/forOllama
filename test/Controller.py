class Controller:
    def __init__(self, model):
        self.model = model

    def process_user_question(self, user_question):
        # 调用模型获取回答
        answer = self.model.ask_glm(user_question)

        # 处理返回的回答
        if answer and 'response' in answer:
            message_content = answer.get('response', '')
            if not message_content:
                message_content = '无法回答问题'
        else:
            message_content = '无法获取答案，请稍后重试。'

        return message_content
