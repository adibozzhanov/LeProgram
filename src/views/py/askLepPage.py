from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.askLepPageQt import Ui_askLepPage
from views.py.askLepWidget import AskLepWidget

class AskLepPage(Ui_askLepPage):
    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)
        self.addAskLepWidget()

    def addAskLepWidget(self, expression = None):
        AskLepWidget(self.askLepWidgetFrame, self.view, None)
