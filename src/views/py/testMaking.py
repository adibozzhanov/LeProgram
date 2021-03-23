from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testMakingQt import Ui_testMakingPage
from views.py.taskMaking import TaskMakingFrame
from views.py.askLepWidget import AskLepWidget


class TestMakingPage(Ui_testMakingPage):
    def __init__(self, master, view):
        self.view = view
        self.tasks = []
        self.setupUi(master)
        self.connectActions()
        self.addAskLepWidget()
        self.addTaskMakingFrame()

    def connectActions(self):
        self.addTaskButton.clicked.connect(lambda: self.addTaskMakingFrame()) # replace with controller things!
       # self.askLepButton.clicked.connect()

    def addAskLepWidget(self, expression=None):
        AskLepWidget(self.askLepWidgetFrame, self.view, None)

    def addTaskMakingFrame(self):
        newFrame = QtWidgets.QFrame()
        self.taskScrollBarContents.addWidget(newFrame)
        self.tasks.append(TaskMakingFrame(newFrame, self.view))