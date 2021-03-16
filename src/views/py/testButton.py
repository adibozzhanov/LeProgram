from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testButtonQt import Ui_testButtonFrame


class TestButton(Ui_testButtonFrame):

    def __init__(self, master, test):
        self.test = test
        self.setupUi(master)
        if self.test != None:
            self.testNameLabel.setText(self.test.getName())
