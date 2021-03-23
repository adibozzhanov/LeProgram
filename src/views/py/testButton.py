from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testButtonQt import Ui_testButtonFrame


class TestButton(Ui_testButtonFrame):

    def __init__(self, master, view, test):
        self.view = view
        self.test = test
        self.setupUi(master)
        if self.test != None:
            self.testNameLabel.setText(self.test.getName())
            self.connectActions()

    def connectActions(self):
            self.viewButton.clicked.connect(lambda: self.view.request("testPreview", self.test))
            self.startButton.clicked.connect(lambda: self.view.request("startTest", self.test))
