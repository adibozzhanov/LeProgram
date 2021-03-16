import sys
import sip
from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.mainQt import Ui_MainWindow
from views.py.home import Home


class View(Ui_MainWindow):

    def run(self):
        self.currentDisplay = None
        self.masterFrame = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.connectActions()
        self.loadHome()
        self.MainWindow.show()
        sys.exit(self.app.exec_())





    def connectActions(self):
        self.homeButton.clicked.connect(self.loadHome)
        self.askLepButton.clicked.connect(self.loadLep)
        self.userButton.clicked.connect(self.loadUser)
        self.randomQsButton.clicked.connect(self.loadRandomQs)
        self.newTestButton.clicked.connect(self.loadNewTest)
        
    def loadHome(self):
        self.cleanMain()
        self.masterFrame = QtWidgets.QFrame()
        self.mainFrameLayout.addWidget(self.masterFrame)
        self.currentDisplay = Home(self.masterFrame)

    def loadNewTest(self):
        self.cleanMain()

        

    def cleanMain(self):
        if self.masterFrame != None:
            self.mainFrameLayout.removeWidget(self.masterFrame)
            sip.delete(self.masterFrame)
            self.masterFrame = None
            self.currentDisplay = None


    def loadLep(self):
        self.cleanMain()

    def loadRandomQs(self):
        self.cleanMain()


    def loadTest(self):

        pass

    def loadUser(self):
        self.cleanMain()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

