"""
Created by SungMin Yoon on 2022/03/28..
Copyright (c) 2022 year SungMin Yoon. All rights reserved.
"""
import sys

from PySide6.QtWidgets import QApplication
from work.window import Window

if __name__ == '__main__':
    print('main')

    app = QApplication(sys.argv)
    window: Window = Window()
    sys.exit(app.exec())
