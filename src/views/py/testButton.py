from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.testButtonQt import Ui_testButtonFrame


class TestButton(Ui_testButtonFrame):

    def __init__(self, master, view, test):
        self.view = view
        self.test = test
<<<<<<< HEAD
=======

>>>>>>> 8095413211d00073c1dccece4e272eee15a36625
        self.setupUi(master)
        if self.test != None:
            self.testNameLabel.setText(self.test.getName())
            self.connectActions()

    def connectActions(self):
            self.viewButton.clicked.connect(lambda: self.view.request("testPreview",self.test))
<<<<<<< HEAD

=======
            self.startButton.clicked.connect(lambda: self.view.request("startTest",self.test))
>>>>>>> 8095413211d00073c1dccece4e272eee15a36625

    def getName(self):
        return self.test.name
