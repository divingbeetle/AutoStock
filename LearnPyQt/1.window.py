import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):  # Inherits QMainWindow, provided by PyQy
    def __init__(self):
        super().__init__()  # Calling parent class' __init__
        self.setWindowTitle("IsWindow")  # Set Title
        self.setGeometry(300, 300, 300, 400)  # Position and Size of the Window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
