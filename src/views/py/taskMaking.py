from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskMakingQt import Ui_taskMakingFrame

class TaskMakingFrame(Ui_taskMakingFrame):
    def __init__(self, master, view, test, taskId):
        self.view = view
        self.test = test
        self.taskId = taskId
        self.setupUi(master)
        self.connectActions()

    def connectActions(self):
        self.deleteButton.clicked.connect(lambda: self.test.remove(taskId))