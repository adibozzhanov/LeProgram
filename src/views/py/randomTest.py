

from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.randomTestQt import Ui_randomTestFrame


class RandomTestFrame(Ui_randomTestFrame):

    def __init__(self, master, view):
        self.view = view
        self.setupUi(master)
