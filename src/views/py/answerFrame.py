from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.answerFrameQt import Ui_answerFrame


class AnswerFrame(Ui_answerFrame):
    def __init__(self, master, view, answer):
        self.view = view
        self.setupUi(master)
        self.answerButton.setText(answer.getExpression().getString())
        
    
