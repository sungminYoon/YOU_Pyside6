"""
Created by SungMin Yoon on 2022/03/28..
Copyright (c) 2022 year SungMin Yoon. All rights reserved.
"""
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import *


class Tool(QToolBar):

    def __init__(self):
        super(Tool, self).__init__()

        self.helpAction = QAction(QIcon(None), 'help', self)
        self.helpAction.triggered.connect(self.help_action_click)

        self.addAction(self.helpAction)

    def help_action_click(self):
        print('Tool: help_action_click')