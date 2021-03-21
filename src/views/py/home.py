from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.homeQt import Ui_mainFrame
from views.py.testButton import TestButton


class Home(Ui_mainFrame):

    def __init__(self, master, view, library):
        self.view = view
        self.testButtons = []
        self.setupUi(master)
        tests = library.getTests()
        if tests != None:
            for test in tests:
                self.addTestWidget(test)

    def addTestWidget(self,test = None):
        newFrame = QtWidgets.QFrame()
        self.testsAreaContents.addWidget(newFrame)
        self.testButtons.append(TestButton(newFrame, self.view, test))
