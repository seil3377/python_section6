import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
#print(sys.argv) #['D:\\Atom_Workspace\\section6\\example\\pyqt_basic_1.py']
label = QLabel("PyQT First Test!")
label.show()

print("Before Loop")
app.exec_()
print("After Loop")
