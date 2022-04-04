"""
Created by SungMin Yoon on 2022/03/31..
Copyright (c) 2022 year SungMin Yoon. All rights reserved.
"""
from PySide6 import QtWidgets, QtCore
from PySide6 import QtGui


class First(QtWidgets.QGraphicsView):

    painter: QtGui.QPainter
    pix_map: QtGui.QPixmap

    def __init__(self):
        super(First, self).__init__()

        # 화면 입니다.
        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()

        # 화면에 장착될 위젯 입니다.
        self.scene.addItem(self.q_graphic)
        self.setScene(self.scene)

        # 픽스 맵 입니다.
        self.pix_map = QtGui.QPixmap(800, 600)
        self.pix_map.fill(QtGui.Qt.white)

        # 픽스 맵 그리기 도구 입니다.
        self.painter = QtGui.QPainter(self.pix_map)

        # 화면에 장착되는 픽스 맵 입니다.
        self.q_graphic.setPixmap(self.pix_map)

    def setup(self):
        self.scene_rect: QtCore.QRectF = QtCore.QRectF(0, 0, 800, 600)
        self.setSceneRect(QtCore.QRectF(self.scene_rect))

    def mouseMoveEvent(self, e):
        print('First: mouseMoveEvent')
        self.painter.drawPoint(e.x(), e.y())
        self.q_graphic.setPixmap(self.pix_map)

    def mouseDoubleClickEvent(self, e):
        print('First: mouseDoubleClickEvent')
        self.pix_map.fill(QtGui.Qt.white)
        self.q_graphic.setPixmap(self.pix_map)