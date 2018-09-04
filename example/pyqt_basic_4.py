import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic #ui complie
from pyqt_basic_ui import Ui_MainWindow

#디자이너에서 ui 작성 > pyuic5 -x pyqt_basic_3.ui -o pyqt_basic_ui.py
#form_class = uic.loadUiType('D:/Atom_Workspace/section6/example/pyqt_basic_3.ui')[0]

class TestForm(QMainWindow, Ui_MainWindow):
#class TestForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
