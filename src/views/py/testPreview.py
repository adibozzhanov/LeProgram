from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.testPreviewQt import Ui_testPreviewFrame
from views.py.taskButton import TaskButton


class TestPreview(Ui_testPreviewFrame):

    def __init__(self, master, test):
        self.test = test
        self.setupUi(master)
        self.initTasks()

    def addTaskWidget(self, task):
        newFrame = QtWidgets.QFrame()
        self.taskAreaLayout.addWidget(newFrame)
        TaskButton(newFrame, task)

    def initTasks(self):
        if self.test != None:
            for task in self.test.getTasks():
                self.addTaskWidget(task)
        else:
            for i in range(20):
                self.addTaskWidget(None)
                
                
            
    
