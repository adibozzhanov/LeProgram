from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskFrameQt import Ui_taskFrame
from views.py.answerFrame import AnswerFrame



class TaskFrame(Ui_taskFrame):

    def __init__(self, master, view, task):
        self.view = view
        self.setupUi(master)
        answers = task.getAnswers()
        self.taskStatementLabel.setText(task.getStatement())
        #self.expressionLabel.setText()
        for Id,answer in answers.items():
            self.addAnswer(answer)

    def addAnswer(self, answer):
        newFrame = QtWidgets.QFrame()
        self.answersLayout.addWidget(newFrame)
        AnswerFrame(newFrame, self.view, answer)
