from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.taskButtonQt import Ui_taskFrame
import random

class TaskButton(Ui_taskFrame):

    def __init__(self, master, task):
        stubNames = ["aloha", "woaah", "nice", "this is a task", "what is a task"]
        self.task = task
        self.setupUi(master)
        if self.task != None:
            self.taskNameLabel.setText(self.task.getName())
        else:
            self.taskNameLabel.setText(random.choice(stubNames))

    def getName(self):
        return self.task.getName()

