""" QT designer is convenient but
you have to write method/ functions handling events on your own
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        # Where did self.pushButton come from?
        # Check QtDesigner's object name

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()