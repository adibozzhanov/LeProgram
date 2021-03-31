from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.randomPageQt import Ui_randomQuestionFrame

class RandomPage(Ui_randomQuestionFrame):
    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)
        self.complexity = 1
        self.startButton.clicked.connect(lambda: self.view.request("startRandomTest", self.getComplexity()))
        self.radioButton.toggled.connect(lambda: self.toggledComplexity(self.radioButton))
        self.radioButton_2.toggled.connect(lambda: self.toggledComplexity(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self.toggledComplexity(self.radioButton_3))
        self.radioButton_4.toggled.connect(lambda: self.toggledComplexity(self.radioButton_4))
        self.radioButton_5.toggled.connect(lambda: self.toggledComplexity(self.radioButton_5))
        self.radioButton_6.toggled.connect(lambda: self.toggledComplexity(self.radioButton_6))

    def toggledComplexity(self, radio):
        if radio.isChecked() == True:
            self.complexity = int(radio.text())

        

    def getComplexity(self):
        return self.complexity

        

        

