from PyQt5 import QtCore, QtGui, QtWidgets
from views.py.notFoundQt import Ui_notFoundFrame


class NotFound(Ui_notFoundFrame):
    def __init__(self,master,view):
        self.view = view
        self.setupUi(master)
        

    
