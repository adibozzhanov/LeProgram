


from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testResultFrameQt import Ui_testResultFrame


class TestResultFrame(Ui_testResultFrame):
    def __init__(self, master, view, test):
        self.master = master
        self.view = view
        self.test = test
        self.setupUi(master)
        self.testNameLabel.setText(test.getName())
        result = test.getScore()
        self.scoreLabel.setText(f"Your score is: {result[0]}/{result[1]}")
