from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testTakingQt import Ui_testTakingFrame
from views.py.taskFrame import TaskFrame



class TestTaking(Ui_testTakingFrame):

    def __init__(self, master, view, test, task = None):
        self.view = view
        self.test = test
        self.tmpFrame = None
        self.setupUi(master)
        self.testNameLabel.setText(test.getName())
        self.test.resetTest()
        self.taskIds = self.test.getTaskIds()
        self.currentTaskIndex = None
        if task is None:#taking the whole test
            if len(self.taskIds)>0 :
                self.currentTaskIndex = 0
                self.__loadTask(self.test.getTask(self.taskIds[0]))
            else:
                self.view.request("testPreview",self.test) # test is empty go back
        else: #viewing one task
            self.__loadTask(task)


    def __loadTask(self, task):
        progression = self.test.getProgression()
        self.progressBar.setProperty("value", progression[0]/progression[1])
        # use task properties and "taskFrame" class to load a new instance of a task on the screen
        # clear the screen before loading new task
        self.clearTask()
        self.tmpFrame = QtWidgets.QFrame()
        self.taskLayout.addWidget(self.tmpFrame)
        TaskFrame(self.tmpFrame, self.view, task)

    def clearTask(self):
        if self.tmpFrame is not None:
            self.taskLayout.removeWidget(self.tmpFrame)
            self.tmpFrame.deleteLater()


    def loadNextTask(self):
        self.currentTaskIndex += 1
        if self.currentTaskIndex == None:
            self.view.request("testPreview",self.test) # only viewing th task: go back to preview
        elif self.currentTaskIndex >= len(self.taskIds):
            self.view.request("testResults",self.test) # out of questions
        else:
            self.__loadTask(self.test.getTask(self.taskIds[self.currentTaskIndex]))
