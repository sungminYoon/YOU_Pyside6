"""
Created by SungMin Yoon on 2022/03/31..
Copyright (c) 2022 year SungMin Yoon. All rights reserved.
"""

from PySide6 import QtCore
from PySide6.QtWidgets import *

from work.view.first import First


class Window_view_controller(QWidget):

    first_view: First

    def __init__(self):
        super().__init__()
        print('Window_view_controller init')

        self.first_view = First()

        self.view_setup()

    def view_setup(self):
        print('Window_view_controller init')

        # 베이스 레이아웃 생성
        from_box = QVBoxLayout()

        # 하위 뷰 레이아웃 생성
        _view = QHBoxLayout()

        # 뷰 레이아웃 에 위젯 장착
        _view.addWidget(self.first_view)

        # 베이스 레이아웃 에 뷰 레이아웃 장착
        from_box.addLayout(_view)

        # 베이스 레이아웃 장착
        self.setLayout(from_box)

