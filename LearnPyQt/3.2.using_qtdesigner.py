""" There are 2 ways for you to convert QT Designer's UI file as a python code
one is to import pyuic
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]


class MyWindow(QMainWindow, form_class):  #  Multiple inheritance
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()