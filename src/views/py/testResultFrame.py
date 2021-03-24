

from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testResultFrameQt.py import Ui_testResultFrame


class TestResultFrame(Ui_testResultFrame):
    def __init__(self, master, view, test):
        self.master = master
        self.view = view
        self.test = test
        self.setupUi(master)
    
