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
        for answerId in answers:
            self.addAnswer(answers[answerId])
            
            
        

    def addAnswer(self, answer):
        newFrame = QtWidgets.QFrame()
        self.answersFrame.addWidget(newFrame)
        AnswerFrame(newFrame, self.view, answer)
        
        
        


    
