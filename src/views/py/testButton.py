from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testButtonQt import Ui_testButtonFrame


class TestButton(Ui_testButtonFrame):

    def __init__(self, master, view, test):
        self.view = view
        self.test = test
        
        self.setupUi(master)
        if self.test != None:
            self.testNameLabel.setText(self.test.getName())
<<<<<<< HEAD
            self.connectActions()

    def connectActions(self):
            self.viewButton.clicked.connect(lambda: self.view.request("testPreview",self.test))
=======
        
            
>>>>>>> 718e3c5baed687603a0dce6877d8e1dd8bf2e0c1

    def getName(self):
        return self.test.name
