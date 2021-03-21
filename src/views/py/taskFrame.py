from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.taskFrameQt import Ui_taskFrame
from views.py.answerFrame import AnswerFrame



class TaskFrame(Ui_taskFrame):

    def __init__(self, master, view, task):
        self.view = view
        self.setupUi(master)

    def addAnswer(self, answer):
        # given the answer instance create the "AnswerFrame" instance in the answerFrame of TaskFrame


    
