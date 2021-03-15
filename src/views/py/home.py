from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.homeQt import Ui_mainFrame


class Home(Ui_mainFrame):

    def __init__(self, master):
        self.setupUi(master)
        
