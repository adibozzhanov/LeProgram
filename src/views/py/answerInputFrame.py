from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.answerInputFrameQt import Ui_answerInputFrame
from models.lexerParser import getExpressionTree

import random

class AnswerInputFrame(Ui_answerInputFrame):

    def __init__(self, master, view, task, answerId):
        self.view = view
        self.answer = task.getAnswer(answerId)
        self.setupUi(master)
        self.connectActions()

    def connectActions(self):
        self.answerInputField.textChanged.connect(lambda: self.addAnswer())

    def addAnswer(self):
        text = self.answerInputField.toPlainText()
        text = text.replace("\n", "")
        text = text.replace("\r", "")
        self.answer.setExpressionFromTree(getExpressionTree(text))