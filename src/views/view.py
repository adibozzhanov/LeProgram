import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.mainQt import Ui_MainWindow
from views.py.home import Home


class View(Ui_MainWindow):

    def run(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.connectActions()

        self.MainWindow.show()
        sys.exit(self.app.exec_())





    def connectActions(self):
        self.homeButton.clicked.connect(self.loadHome)
        
    def loadHome(self):
        self.cleanMain()
        self.currenctDisplay = Home(self.MainFrame)
        self.MainFrame.show()

        

    def cleanMain(self):

        pass


    def loadLep(self):

        pass

    def loadTest(self):

        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

