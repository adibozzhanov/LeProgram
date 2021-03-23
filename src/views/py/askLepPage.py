from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.askLepPageQt import Ui_askLepPage
from views.py.askLepWidget import AskLepWidget

class AskLepPage(Ui_askLepPage):
    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)
        self.connectedActions()
        self.tmpFrame = None
    def connectedActions(self):
        self.searchButton.clicked.connect(self.requestExpression)

    def requestExpression(self):
        self.expressionInput.toPlainText()

    def updateAskLep(self, expression = None):
        self.deleteAskLep()
        self.tmpFrame = QtWidgets.QFrame()
        self.askLepLayout.addWidget(self.tmpFrame)
        AskLepWidget(self.askLepWidgetFrame, self.view, expression)

    def deleteAskLep(self):
        if self.tmpFrame != None:
            self.askLepLayout.removeWidget(self.tmpFrame)
            self.tmpFrame.deleteLater()
        
