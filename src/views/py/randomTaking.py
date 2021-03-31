from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.randomTakingQt import Ui_randomTakingFrame
from views.py.taskFrame import TaskFrame
from views.py.askLepWidget import AskLepWidget

class RandomTest(Ui_randomTakingFrame):

    def __init__(self, master, view, task, score, total, complexity):
        self.master = master
        self.view = view
        self.complexity = complexity
        self.task = task
        self.score = score
        self.total = total
        self.setupUi(master)
        self.scoreLabel.setText(f"Score: {self.score}/{self.total}")
        newFrame = QtWidgets.QFrame(self.taskFrame)
        self.taskLayout.addWidget(newFrame)
        TaskFrame(newFrame, view, task, self, True)
        tmpFrame = QtWidgets.QFrame(self.askLepFrame)
        self.askLepLayout.addWidget(tmpFrame)
        self.askLep = AskLepWidget(tmpFrame, view, None)
        self.hideAskLep()
        self.nextQButton.clicked.connect(self.loadNextTask)

    def hideAskLep(self):
        self.askLepFrame.hide()

    def showAskLep(self):
        self.askLepFrame.show()

    def updateAskLep(self, expression = None):
        self.showAskLep()
        self.askLep.setExpressionInfo(expression)

    def loadNextTask(self):
        self.view.request("startRandomTest", self.complexity, self.score, self.total + 1)

        
        
