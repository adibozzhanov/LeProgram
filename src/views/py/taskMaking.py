from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskMakingQt import Ui_taskMakingFrame

class TaskMakingFrame(Ui_taskMakingFrame):
    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)