"""
Created by SungMin Yoon on 2022/03/28..
Copyright (c) 2022 year SungMin Yoon. All rights reserved.
"""
from PySide6.QtWidgets import *

from .window_view_controller import Window_view_controller
from work.view.tool import Tool


class Window(QMainWindow):

    window_view_controller: Window_view_controller

    tool: Tool      # 툴바 입니다.

    def __init__(self):
        super(Window, self).__init__()

        self.tool = Tool()
        self.window_view_controller = Window_view_controller()

        self.addToolBar(self.tool)
        self.setCentralWidget(self.window_view_controller)
        self.show()