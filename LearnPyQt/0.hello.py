import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  # Class -> instance
# print(sys.argv) sys.argv will be a abs path for the code
label = QLabel("Hello PyQt")
label.show()
app.exec_()
# Entering event loop by calling exec method
# event loop is a infinite loop that handles events
