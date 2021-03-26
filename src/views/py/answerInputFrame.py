from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.answerInputFrameQt import Ui_answerInputFrame
from models.lexerParser import getExpressionTree
from models.expression import Expression

import random


class AnswerInputFrame(Ui_answerInputFrame):

    def __init__(self, master, view):
        self.view = view
        self.answer = (None, False)
        self.setupUi(master)
        self.connectActions()

    def getAnswer(self):
        return self.answer

    def connectActions(self):
        self.answerInputField.textChanged.connect(lambda: self.addAnswer())
        self.ifCorrectCheckBox.toggled.connect(lambda: self.changeCorrect())

    def addAnswer(self):
        text = self.answerInputField.toPlainText()
        text = text.replace("\n", "")
        text = text.replace("\r", "")
        tree = getExpressionTree(text)

        if tree is None:
            self.setInvalidLabel()
        else:
            self.answer = (Expression(tree), self.answer[1])
            self.setValidLabel()

    def setInvalidLabel(self):
        self.ifValidLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.ifValidLabel.setText("Invalid Expression")

    def setValidLabel(self):
        self.ifValidLabel.setStyleSheet("color: rgb(50, 168, 82);")
        self.ifValidLabel.setText("Valid Expression")

    def changeCorrect(self):
        val = True if self.ifCorrectCheckBox.isChecked() else False
        self.answer = (self.answer[0], val)


