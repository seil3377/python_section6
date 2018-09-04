import sys
from PyQt5.QtWidgets import * #PyQT5.QtWidgets.QMainWindow
from PyQt5.QtCore import *

#PyQT : 대기상태
#시그널(이벤트 발생)
#SLOT(이벤트처리)

class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800,400,500,300) #xywh

        btn_1 = QPushButton("Click1", self)
        btn_2 = QPushButton("Click2", self)
        btn_3 = QPushButton("Click3", self)

        btn_1.move(20, 20)
        btn_2.move(20, 60)
        btn_3.move(20, 100)

        btn_1.clicked.connect(self.btn_1_clicked) #시그널발생.슬롯연결(함수)
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)

    def btn_1_clicked(self):
        QMessageBox.about(self,"message","clicked")

    def btn_2_clicked(self):
        print("Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
