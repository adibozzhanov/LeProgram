import sys
from views.main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


# Frames:
# Main Frame - gets constanty reloaded by user's actions
# Top Frame - always there on top





class View:
    def __init__(self):

        # key  
        self.displays = {} 
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

    


    def run(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())


    def updateMain(self, displayName):
        # clears the main frame and loads new widgets in it
        pass


    def cleanMain(self):
        # removes all elements from the main frame
        
        pass
