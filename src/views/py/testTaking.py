from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testTakingQt import Ui_testTakingFrame



class TestTaking(Ui_testTakingFrame):

    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)


    def loadTask(self, task):
        # use task properties and "taskFrame" class to load a new instance of a task on the screen
        # clear the screen before loading new task
        pass
