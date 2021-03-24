from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testMakingQt import Ui_testMakingPage
from views.py.taskMaking import TaskMakingFrame
from views.py.askLepWidget import AskLepWidget
import models.library
import models.test
import models.model


class TestMakingPage(Ui_testMakingPage):
    def __init__(self, master, view, library):
        self.view = view
        self.testID = library.addNewTestAndGetId()
        self.test = library.getTest(self.testID)

        self.taskIDs = []
        self.setupUi(master)
        self.connectActions()
        self.addAskLepWidget()
        self.addTaskMakingFrame()

    def connectActions(self):
        self.addTaskButton.clicked.connect(lambda: self.addTaskMakingFrame())
        self.testNameInput.textChanged.connect(lambda: self.renameTest())
       # self.askLepButton.clicked.connect()

    def addAskLepWidget(self, expression=None):
        AskLepWidget(self.askLepWidgetFrame, self.view, None)

    def addTaskMakingFrame(self):
        newFrame = QtWidgets.QFrame()
        self.taskScrollBarContents.addWidget(newFrame)
        self.taskIDs.append(self.test.addNewTaskAndGetId())
        TaskMakingFrame(newFrame, self.view, self.test, self.taskIDs[-1])

    def renameTest(self):
        text = self.testNameInput.toPlainText()
        text.replace("\n","")
        text.replace("\r", "")
        self.test.setName(text)
        self.testNameLabel.setText(text)