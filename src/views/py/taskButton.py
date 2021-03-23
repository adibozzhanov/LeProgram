from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.taskButtonQt import Ui_taskFrame
import random

class TaskButton(Ui_taskFrame):

    def __init__(self, master, view, test, task):
        stubNames = ["aloha", "woaah", "nice", "this is a task", "what is a task"]
        self.task = task
        self.view = view
        self.test = test
        self.setupUi(master)
        if self.task is not None:
            self.connectActions()
            self.taskNameLabel.setText(self.task.getStatement()) #task does not really have a name soo i put this in for now
        else: #wait how could a task be none?
            self.taskNameLabel.setText(random.choice(stubNames))

    def connectActions(self):
            self.viewButton.clicked.connect(lambda: self.view.request("startTest", self.test, self.task))

    def getName(self):
        return self.task.getName()

    def setName(self, name):
        self.taskNameLabel.setText(name)
