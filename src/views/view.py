import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.mainQt import Ui_MainWindow
from views.py.home import Home
from views.py.testPreview import TestPreview
from views.py.randomPage import RandomPage
from views.py.askLepPage import AskLepPage
from views.py.notFound import NotFound

class View(Ui_MainWindow):
    
    def __init__(self):
        self.request = None
        self.currentDisplay = None
        self.masterFrame = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.connectActions()
    

    def run(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def connectActions(self):
        self.homeButton.clicked.connect(lambda: self.request("homePage"))
        self.askLepButton.clicked.connect(lambda: self.request("askLep"))
        self.userButton.clicked.connect(lambda: self.request("user"))
        self.randomQsButton.clicked.connect(lambda: self.request("randomQuestions"))
        self.newTestButton.clicked.connect(lambda:self.request("newTest"))
        

        
    def registerRequestHandler(self, handler):
        # called by controller
        # assigns request handler controller method to "self.request"
        self.request = handler        


        
    def loadHome(self, library):
        self.cleanMain()
        self.currentDisplay = Home(self.masterFrame, self, library)

    def loadNewTest(self):
        self.cleanMain()

    def cleanMain(self):
        if self.masterFrame != None:
            self.mainFrameLayout.removeWidget(self.masterFrame)
            self.masterFrame.deleteLater()
        self.masterFrame = QtWidgets.QFrame()
        self.mainFrameLayout.addWidget(self.masterFrame)
            
    def loadLep(self):
        self.cleanMain()
        self.currentDisplay = AskLepPage(self.masterFrame, self)

    def loadRandomQs(self):
        self.cleanMain()
        self.currentDisplay = RandomPage(self.masterFrame, self)
        

    def loadTestPreview(self, test = None):
        self.cleanMain()
        self.currentDisplay = TestPreview(self.masterFrame, None)

    def loadNotFound(self):
        self.cleanMain()
        self.currentDisplay = NotFound(self.masterFrame, self)

    def loadUser(self):
        self.cleanMain()

