from Controller import Controller
from Model import Model
from View import View

if __name__ == "__main__":
    # 创建模型、控制器和视图
    model = Model()
    controller = Controller(model)
    view = View(controller)

    # 启动 Gradio 界面
    view.launch()
