from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.askLepWidgetQt import Ui_askLepWidgetFrame


class AskLepWidget(Ui_askLepWidgetFrame):

    def __init__(self, master, view, expression):
        self.view = view
        self.expression = expression
        self.setupUi(master)
