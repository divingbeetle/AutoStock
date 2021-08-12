import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IsWindow")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click me", self)  # Make instance
        btn1.move(20, 20)  # Adjusting Position w/ move method
        btn1.clicked.connect(self.btn1_clicked)  # Connect event and event handling method w/ method 'connect'

    def btn1_clicked(self):  # Method to handle event, 'clicked' AKA slot, slot is a method called w/ certain signal
        #  Other programing languages call this kind of function as callback function
        QMessageBox.about(self, "message", "clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
