from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testTakingQt import Ui_testTakingFrame
from views.py.taskFrame import TaskFrame
from views.py.askLepWidget import AskLepWidget


class TestTaking(Ui_testTakingFrame):

    
    def __init__(self, master, view, test, task = None):
        self.view = view
        self.test = test
        self.tmpFrame = None
        self.askLePtmpFrame = None
        self.setupUi(master)
        self.connectActions()
        self.testNameLabel.setText(test.getName())
        self.test.resetTest()
        self.taskIds = self.test.getTaskIds()
        self.currentTaskIndex = None

        tmpFrame = QtWidgets.QFrame(self.askLepFrame)
        self.askLepLayout.addWidget(tmpFrame)
        self.askLep = AskLepWidget(tmpFrame, view, None)
        self.hideAskLep()
        
        if task is None:#taking the whole test
            if len(self.taskIds)>0 :
                self.currentTaskIndex = 0
                self.__loadTask(self.test.getTask(self.taskIds[0]))
            else:
                self.view.request("testPreview",self.test) # test is empty go back
        else: #viewing one task
            self.nextQButton.setText("go back")
            self.__loadTask(task)
            self.nextQButton.setEnabled(True)

            
    def connectActions(self):
        self.nextQButton.clicked.connect(self.loadNextTask)

    def hideAskLep(self):
        self.askLepFrame.hide()

    def showAskLep(self):
        self.askLepFrame.show()

    def updateAskLep(self, expression = None):
        self.showAskLep()
        self.askLep.setExpressionInfo(expression)


    def __loadTask(self, task):
        progression = self.test.getProgression()
        val = progression[0]/progression[1]
        self.progressBar.setProperty("value", val*100)
        # use task properties and "taskFrame" class to load a new instance of a task on the screen
        # clear the screen before loading new task
        self.clearTask()
        self.tmpFrame = QtWidgets.QFrame()
        self.taskLayout.addWidget(self.tmpFrame)
        TaskFrame(self.tmpFrame, self.view, task, self)
        self.nextQButton.setEnabled(False)
        




    def clearTask(self):
        if self.tmpFrame is not None:
            self.taskLayout.removeWidget(self.tmpFrame)
            self.tmpFrame.deleteLater()

    def loadNextTask(self):
        self.hideAskLep()
        if self.currentTaskIndex is not None:
            self.currentTaskIndex += 1
            if self.currentTaskIndex == None:
                self.view.request("testPreview", self.test) # only viewing th task: go back to preview
            elif self.currentTaskIndex >= len(self.taskIds):
                self.view.request("loadTestResultsPls", self.test) # out of questions
            else:
                self.__loadTask(self.test.getTask(self.taskIds[self.currentTaskIndex]))
        else:
            self.view.request("testPreview", self.test)
