from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.testPreviewQt import Ui_testPreviewFrame
from views.py.taskButton import TaskButton


class TestPreview(Ui_testPreviewFrame):

    def __init__(self, master,view, test):
        self.view = view
        self.test = test
        self.taskCount = 0
        self.numTasks = 0
        self.setupUi(master)
        self.testNameLabel.setText(self.test.getName())
        self.initTasks()

    def addTaskWidget(self, task):
        newFrame = QtWidgets.QFrame()
        self.taskAreaLayout.insertWidget(self.taskCount,newFrame)
        t = TaskButton(newFrame, self.view, self.test, task)
        self.taskCount += 1
        t.setName(f"Question#{self.taskCount}")

    def initTasks(self):
        if self.test is not None:
            tasks = self.test.getTasks()
            self.numTasks = len(tasks)
            for id,task in tasks.items():
                self.addTaskWidget(task)
        else:
            for i in range(20):
                self.addTaskWidget(None)
