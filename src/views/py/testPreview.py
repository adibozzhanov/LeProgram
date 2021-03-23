from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.testPreviewQt import Ui_testPreviewFrame
from views.py.taskButton import TaskButton


class TestPreview(Ui_testPreviewFrame):

    def __init__(self, master,view, test):
        self.view = view
        self.test = test
        self.taskCount = 1
        self.setupUi(master)
        self.initTasks()

    def addTaskWidget(self, task):
        newFrame = QtWidgets.QFrame()
        self.taskAreaLayout.addWidget(newFrame)
        t = TaskButton(newFrame, self.view, task)
        t.setName(f"Question#{self.taskCount}")
        self.taskCount += 1

    def initTasks(self):
        if self.test != None:
            tasks = self.test.getTasks()
            for task in tasks:
                self.addTaskWidget(tasks[task])
                
        else:
            for i in range(20):
                self.addTaskWidget(None)
                
                
            
    
