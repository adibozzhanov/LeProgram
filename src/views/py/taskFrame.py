from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskFrameQt import Ui_taskFrame
from views.py.answerFrame import AnswerFrame



class TaskFrame(Ui_taskFrame):

    def __init__(self, master, view, task, testFrame):
        self.view = view
        self.setupUi(master)
        self.testFrame = testFrame
        self.task = task
        answers = task.getAnswers()
        self.answerFrames = []
        self.taskStatementLabel.setText(task.getStatement())
        self.expressionLabel.setText(task.getExpressionString())
        for Id,answer in answers.items():
            self.addAnswer(answer)

    def addAnswer(self, answer):
        newFrame = QtWidgets.QFrame()
        self.answersLayout.addWidget(newFrame)
        tmp = AnswerFrame(newFrame, self.view, answer, self)
        self.answerFrames.append(tmp)

    def checkAnswers(self, answerId):
        for answerFrame in self.answerFrames:
            if answerFrame.answer.getIsCorrect():
                answerFrame.answerButton.setStyleSheet("background-color : green")
        self.testFrame.test.addTaskAnswerGiven(self.task.getTaskId(), answerId)
        self.testFrame.nextQButton.setEnabled(True)
