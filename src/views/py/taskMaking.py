from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskMakingQt import Ui_taskMakingFrame
from views.py.answerInputFrame import AnswerInputFrame
from models.lexerParser import getExpressionTree


class TaskMakingFrame(Ui_taskMakingFrame):
    def __init__(self, master, view, test, taskId):
        self.master = master
        self.view = view
        self.task = test.getTask(taskId)
        self.answerIDs = []
        self.answerFrames = []
        self.setupUi(master)
        self.addAnswer()
        self.connectActions()

    def connectActions(self):
        self.deleteButton.clicked.connect(lambda: self.removeTask())
        self.addAnswerButton.clicked.connect(lambda: self.addAnswer())
        self.removeAnswerButton.clicked.connect(lambda: self.removeAnswer())
        self.taskDescriptionInput.textChanged.connect(lambda: self.addTaskDescription())
        self.expressionInput.textChanged.connect(lambda: self.addExpression())

    def removeTask(self):
        self.test.removeTask(self.taskId)
        self.master.deleteLater()

    def addAnswer(self):
        newFrame = QtWidgets.QFrame()
        newFrame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        newFrame.setMinimumSize(QtCore.QSize(0, 150))
        self.answerScrollBarContents.addWidget(newFrame)
        self.answerIDs.append(self.task.addNewAnswerAndGetId())
        self.answerFrames.append(newFrame)
        AnswerInputFrame(newFrame, self.view, self.task, self.answerIDs[-1])

    def removeAnswer(self):
        if len(self.answerIDs) > 1:
            self.task.removeAnswer(self.answerIDs[-1])
            self.answerIDs.pop()
            self.answerFrames[-1].deleteLater()
            self.answerFrames.pop()

    def addTaskDescription(self):
        text = self.taskDescriptionInput.toPlainText()
        self.task.setStatement(text)

    def addExpression(self):
        text = self.expressionInput.text()
        tree = getExpressionTree(text)
        self.task.setExpressionFromTree(tree)
