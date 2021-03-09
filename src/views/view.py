import sys
from views.main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class View:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.pushButton.clicked.connect(self.changeLabel)
        
    def run(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())


    def changeLabel(self):
        self.ui.label.setText("My label")

    
