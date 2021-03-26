from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testMakingQt import Ui_testMakingPage
from views.py.taskMaking import TaskMakingFrame
from views.py.askLepWidget import AskLepWidget

class TestMakingPage(Ui_testMakingPage):
    def __init__(self, master, view, library):
        self.view = view
        self.test = ["TestName", "TestDescription", []]
        self.numTasks = 0
        self.taskFrames = []
        self.taskMakingFrames = []

        self.setupUi(master)
        self.connectActions()
        self.addAskLepWidget()
        self.addTaskMakingFrame()

    def getTest(self):
        for task in self.taskMakingFrames:
            self.test[2].append(task.getTask())
        self.view.request("saveTest", self.test)

    def connectActions(self):
        self.addTaskButton.clicked.connect(lambda: self.addTaskMakingFrame())
        self.testNameInput.textChanged.connect(lambda: self.renameTest())
        self.testDescriptionInput.textChanged.connect(lambda: self.addDescription())
        self.finishButton.clicked.connect(lambda: self.getTest())
        # self.askLepButton.clicked.connect()

    def addAskLepWidget(self, expression=None):
        AskLepWidget(self.askLepWidgetFrame, self.view, None)

    def addTaskMakingFrame(self):
        newFrame = QtWidgets.QFrame()
        self.taskScrollBarContents.addWidget(newFrame)
        self.taskFrames.append(newFrame)
        self.taskMakingFrames.append(TaskMakingFrame(newFrame, self.view, self, self.numTasks))
        self.numTasks += 1

    def deleteTaskMakingFrame(self, index):
        self.taskFrames[index].deleteLater()
        del self.taskFrames[index]
        del self.taskMakingFrames[index]
        for c in range(index, len(self.taskFrames) - 1):
            self.taskFrames[c].decreaseIndex()
            self.taskMakingFrames[c].decreaseIndex()
        self.numTasks -= 1

    def renameTest(self):
        text = self.testNameInput.toPlainText()
        text = text.replace("\n","")
        text = text.replace("\r","")
        self.test[0] = text
        self.testNameLabel.setText(text)

    def addDescription(self):
        text = self.testDescriptionInput.toPlainText()
        self.test[1] = text