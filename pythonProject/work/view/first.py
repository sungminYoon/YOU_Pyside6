"""
Created by SungMin Yoon on 2022/03/31..
Copyright (c) 2022 year SungMin Yoon. All rights reserved.
"""
from PySide6 import QtWidgets, QtCore
from PySide6 import QtGui


class First(QtWidgets.QGraphicsView):

    def __init__(self):
        super(First, self).__init__()

        self.scene = QtWidgets.QGraphicsScene(self)
        self.q_graphic = QtWidgets.QGraphicsPixmapItem()

        self.scene.addItem(self.q_graphic)
        self.setScene(self.scene)

        pix_map = QtGui.QPixmap(800, 600)
        pix_map.fill(QtGui.Qt.white)
        self.q_graphic.setPixmap(pix_map)

    def setup(self):
        self.scene_rect: QtCore.QRectF = QtCore.QRectF(0, 0, 800, 600)
        self.setSceneRect(QtCore.QRectF(self.scene_rect))