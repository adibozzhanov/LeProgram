# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/testMaking.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testMakingPage(object):
    def setupUi(self, testMakingPage):
        testMakingPage.setObjectName("testMakingPage")
        testMakingPage.resize(1221, 789)
        self.gridLayout = QtWidgets.QGridLayout(testMakingPage)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.addTaskButton = QtWidgets.QPushButton(testMakingPage)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.addTaskButton.setFont(font)
        self.addTaskButton.setObjectName("addTaskButton")
        self.gridLayout.addWidget(self.addTaskButton, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 5, 1, 1)
        self.finishButton = QtWidgets.QPushButton(testMakingPage)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.finishButton.setFont(font)
        self.finishButton.setObjectName("finishButton")
        self.gridLayout.addWidget(self.finishButton, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.testNameLabel = QtWidgets.QLabel(testMakingPage)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.gridLayout.addWidget(self.testNameLabel, 1, 1, 1, 2)
        self.taskMakingScrollArea = QtWidgets.QScrollArea(testMakingPage)
        self.taskMakingScrollArea.setWidgetResizable(True)
        self.taskMakingScrollArea.setObjectName("taskMakingScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 395, 570))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.taskMakingScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.taskMakingScrollArea, 5, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.askLepWidgetFrame = QtWidgets.QFrame(testMakingPage)
        self.askLepWidgetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.askLepWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        self.gridLayout.addWidget(self.askLepWidgetFrame, 0, 4, 6, 1)

        self.retranslateUi(testMakingPage)
        QtCore.QMetaObject.connectSlotsByName(testMakingPage)

    def retranslateUi(self, testMakingPage):
        _translate = QtCore.QCoreApplication.translate
        testMakingPage.setWindowTitle(_translate("testMakingPage", "Frame"))
        self.addTaskButton.setText(_translate("testMakingPage", "Add Task"))
        self.finishButton.setText(_translate("testMakingPage", "Finish"))
        self.testNameLabel.setText(_translate("testMakingPage", "Test Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testMakingPage = QtWidgets.QFrame()
    ui = Ui_testMakingPage()
    ui.setupUi(testMakingPage)
    testMakingPage.show()
    sys.exit(app.exec_())