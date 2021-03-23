from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.taskButtonQt import Ui_taskFrame
import random

class TaskButton(Ui_taskFrame):

    def __init__(self, master, view, task):
        self.task = task
        self.setupUi(master)
        
    def setName(self, name):
        self.taskNameLabel.setText(name)

