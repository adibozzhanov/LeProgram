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

    def onClick(self):
        if self.answer.getIsCorrect():
            self.answerButton.setStyleSheet("background-color : green")
        else:
            self.answerButton.setStyleSheet("background-color : red")
        
        self.taskFrame.checkAnswers(self.answer.getAnswerId())
        
        
    
