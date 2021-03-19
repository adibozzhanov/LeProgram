from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.randomPageQt import Ui_randomQuestionFrame

class RandomPage(Ui_randomQuestionFrame):
    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)

