from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.randomPageQt import Ui_randomQuestionFrame

class RandomPage(Ui_randomQuestionFrame):
    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)
        self.startButton.clicked.connect(lambda: self.view.request("startRandomTest", self.getComplexity()))
        self.radioButtons = []
        self.radioButtons.append(self.radioButton)
        self.radioButtons.append(self.radioButton_2)
        self.radioButtons.append(self.radioButton_3)
        self.radioButtons.append(self.radioButton_4)
        self.radioButtons.append(self.radioButton_5)
        self.radioButtons.append(self.radioButton_6)
        
        for radio in self.radioButtons:
            radio.toggled.connect(lambda: self.toggledComplexity())


    def toggledComplexity(self):

        pass

    def getComplexity(self):
        pass 

        

        

