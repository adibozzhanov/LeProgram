import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.mainQt import Ui_MainWindow
from views.py.home import Home
from views.py.testPreview import TestPreview
from views.py.randomPage import RandomPage

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

    def connectTestPreview(self, button):
        button.clicked.connect(self.loadTestPreview)
        
        
    def loadHome(self):
        self.cleanMain()
        self.masterFrame = QtWidgets.QFrame()
        self.mainFrameLayout.addWidget(self.masterFrame)
        self.currentDisplay = Home(self.masterFrame, self)

    def loadNewTest(self):
        self.cleanMain()

    def cleanMain(self):
        if self.masterFrame != None:
            self.mainFrameLayout.removeWidget(self.masterFrame)
            self.masterFrame.deleteLater()
            self.masterFrame = None
            self.currentDisplay = None
            
    def loadLep(self):
        self.cleanMain()

    def loadRandomQs(self):
        self.cleanMain()
        self.masterFrame = QtWidgets.QFrame()
        self.mainFrameLayout.addWidget(self.masterFrame)
        self.currentDisplay = RandomPage(self.masterFrame, self)
        

    def loadTestPreview(self, test = None):
        self.cleanMain()
        self.masterFrame = QtWidgets.QFrame()
        self.mainFrameLayout.addWidget(self.masterFrame)
        self.currentDisplay = TestPreview(self.masterFrame, None)




    def loadUser(self):
        self.cleanMain()

