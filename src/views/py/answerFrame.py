from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.answerFrameQt import Ui_answerFrame


class AnswerFrame(Ui_answerFrame):
    def __init__(self, master, view, answer, taskFrame):
        self.taskFrame = taskFrame
        self.view = view
        self.setupUi(master)
        self.answer = answer
        self.answerButton.setText(answer.getExpression().getDisplayString())
        self.answerButton.clicked.connect(self.onClick)
        self.isAnswered = False

    def onClick(self):
        if not self.isAnswered:
            if self.answer.getIsCorrect():
                self.answerButton.setStyleSheet("background-color : rgb(23, 161, 145)")
                if self.taskFrame.randomTest:
                    self.taskFrame.testFrame.score += 1
            else:
                self.answerButton.setStyleSheet("background-color : rgb(204, 54, 20)")
            self.taskFrame.checkAnswers(self.answer.getAnswerId())
        else:
            self.taskFrame.testFrame.updateAskLep(self.answer.getExpression())
