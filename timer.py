from PyQt5.QtWidgets import *

from PyQt5.QtCore import QTimer

import pyqtgraph as pg

import numpy as np

from pandas import read_csv


class App(QWidget):

    def __init__(self):

        super().__init__()

        self.timer = QTimer()

        self.grid = QGridLayout()

        self.graph1 = pg.PlotWidget(self, 'k')

        self.grid.addWidget(self.graph1, 0, 0, 3, 3)

        self.setLayout(self.grid)

        self.timer.timeout.connect(self.function)

        self.show()

        self.setGeometry(700, 100, 600, 400)

        self.timer.start(10)


    def function(self):

        self.graph1.plotItem.clear()

        self.data1 = read_csv("E:/Practical projects/Damped.csv", header = None)

        self.graph1.plotItem.plot(self.data1["t"], self.data1["e^(-βt)*cosx"], pen = pg.mkPen('y'))




app = QApplication([])

a = App()


app.exec_()