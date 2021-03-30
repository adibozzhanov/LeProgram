from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskMakingQt import Ui_taskMakingFrame
from views.py.answerInputFrame import AnswerInputFrame
from models.lexerParser import getExpressionTree
from models.expression import Expression


class TaskMakingFrame(Ui_taskMakingFrame):
    def __init__(self, master, view, parent, index):
        self.view = view
        self.task = ["Task statement", "Task expression", []]
        self.index = index
        self.parent = parent
        self.numAnswers = 0
        self.answerFrames = []
        self.answerMakingFrames = []
        self.setupUi(master)
        self.addAnswer()
        self.connectActions()

    def getTask(self):
        for c in range(self.numAnswers):
            answer = self.answerMakingFrames[c].getAnswer()
            if answer[0] is None:
                continue
            else:
                self.task[2].append(answer)
        return self.task

    def connectActions(self):
        self.deleteButton.clicked.connect(lambda: self.removeTask())
        self.addAnswerButton.clicked.connect(lambda: self.addAnswer())
        self.removeAnswerButton.clicked.connect(lambda: self.removeAnswer())
        self.taskDescriptionInput.textChanged.connect(lambda: self.addTaskDescription())
        self.expressionInput.textChanged.connect(lambda: self.addExpression())

    def removeTask(self):
        self.parent.deleteTaskMakingFrame(self.index)

    def addAnswer(self):
        newFrame = QtWidgets.QFrame()
        self.answerScrollBarContents.addWidget(newFrame)
        self.answerFrames.append(newFrame)
        self.answerMakingFrames.append(AnswerInputFrame(newFrame, self.view))
        self.numAnswers += 1

    def decreaseIndex(self):
        self.index -= 1

    def removeAnswer(self):
        if len(self.answerFrames) > 1:
            self.answerFrames[-1].deleteLater()
            self.answerFrames.pop()
            self.answerMakingFrames.pop()
            self.numAnswers -= 1

    def addTaskDescription(self):
        text = self.taskDescriptionInput.toPlainText()
        self.task[0] = text

    def addExpression(self):
        text = self.expressionInput.text()
        text = text.replace(" ", "")
        tree = getExpressionTree(text)
        if tree is not None or text == "":
            self.task[1] = Expression(tree)
            self.setValidLabel()
        else:
            self.setInvalidLabel()

    def setInvalidLabel(self):
        self.ifValidLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.ifValidLabel.setText("Invalid")

    def setValidLabel(self):
        self.ifValidLabel.setStyleSheet("color: rgb(50, 168, 82);")
        self.ifValidLabel.setText("Valid")
