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
        testMakingPage.resize(1219, 649)
        testMakingPage.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);")
        self.gridLayout = QtWidgets.QGridLayout(testMakingPage)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.testNameInput = QtWidgets.QPlainTextEdit(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testNameInput.sizePolicy().hasHeightForWidth())
        self.testNameInput.setSizePolicy(sizePolicy)
        self.testNameInput.setMinimumSize(QtCore.QSize(100, 0))
        self.testNameInput.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.testNameInput.setFont(font)
        self.testNameInput.setStyleSheet("border-color: rgb(246, 247, 200)")
        self.testNameInput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.testNameInput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.testNameInput.setLineWidth(0)
        self.testNameInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.testNameInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.testNameInput.setObjectName("testNameInput")
        self.gridLayout.addWidget(self.testNameInput, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 5, 1, 1)
        self.taskMakingScrollArea = QtWidgets.QScrollArea(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskMakingScrollArea.sizePolicy().hasHeightForWidth())
        self.taskMakingScrollArea.setSizePolicy(sizePolicy)
        self.taskMakingScrollArea.setMinimumSize(QtCore.QSize(500, 200))
        self.taskMakingScrollArea.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.taskMakingScrollArea.setStyleSheet("border-color: rgb(246, 247, 200);\n"
"background-color: rgb(246, 247, 200);")
        self.taskMakingScrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.taskMakingScrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskMakingScrollArea.setLineWidth(1)
        self.taskMakingScrollArea.setWidgetResizable(True)
        self.taskMakingScrollArea.setObjectName("taskMakingScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 531, 384))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.taskScrollBarContents = QtWidgets.QVBoxLayout()
        self.taskScrollBarContents.setSpacing(24)
        self.taskScrollBarContents.setObjectName("taskScrollBarContents")
        self.verticalLayout_2.addLayout(self.taskScrollBarContents)
        self.taskMakingScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.taskMakingScrollArea, 13, 1, 1, 4)
        self.testDescriptionInput = QtWidgets.QPlainTextEdit(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testDescriptionInput.sizePolicy().hasHeightForWidth())
        self.testDescriptionInput.setSizePolicy(sizePolicy)
        self.testDescriptionInput.setMinimumSize(QtCore.QSize(100, 60))
        self.testDescriptionInput.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.testDescriptionInput.setFont(font)
        self.testDescriptionInput.setStyleSheet("border-color: rgb(246, 247, 200)")
        self.testDescriptionInput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.testDescriptionInput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.testDescriptionInput.setLineWidth(0)
        self.testDescriptionInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.testDescriptionInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.testDescriptionInput.setTabChangesFocus(False)
        self.testDescriptionInput.setPlainText("")
        self.testDescriptionInput.setObjectName("testDescriptionInput")
        self.gridLayout.addWidget(self.testDescriptionInput, 7, 1, 1, 1)
        self.askLepWidgetFrame = QtWidgets.QFrame(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepWidgetFrame.sizePolicy().hasHeightForWidth())
        self.askLepWidgetFrame.setSizePolicy(sizePolicy)
        self.askLepWidgetFrame.setMinimumSize(QtCore.QSize(100, 400))
        self.askLepWidgetFrame.setMaximumSize(QtCore.QSize(900, 16777215))
        self.askLepWidgetFrame.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"")
        self.askLepWidgetFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.askLepWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepWidgetFrame.setLineWidth(2)
        self.askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        self.gridLayout.addWidget(self.askLepWidgetFrame, 0, 6, 14, 1)
        self.testNameLabel = QtWidgets.QLabel(testMakingPage)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setLineWidth(0)
        self.testNameLabel.setObjectName("testNameLabel")
        self.gridLayout.addWidget(self.testNameLabel, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 1)
        self.addTaskButton = QtWidgets.QPushButton(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTaskButton.sizePolicy().hasHeightForWidth())
        self.addTaskButton.setSizePolicy(sizePolicy)
        self.addTaskButton.setMinimumSize(QtCore.QSize(0, 68))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addTaskButton.setFont(font)
        self.addTaskButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.addTaskButton.setObjectName("addTaskButton")
        self.gridLayout.addWidget(self.addTaskButton, 8, 3, 1, 1)
        self.finishButton = QtWidgets.QPushButton(testMakingPage)
        self.finishButton.setMinimumSize(QtCore.QSize(0, 68))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.finishButton.setFont(font)
        self.finishButton.setStyleSheet("background-color: rgb(255, 253, 78);\n"
"border-color: rgb(255, 253, 78);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        self.finishButton.setObjectName("finishButton")
        self.gridLayout.addWidget(self.finishButton, 8, 4, 1, 1)

        self.retranslateUi(testMakingPage)
        QtCore.QMetaObject.connectSlotsByName(testMakingPage)

    def retranslateUi(self, testMakingPage):
        _translate = QtCore.QCoreApplication.translate
        testMakingPage.setWindowTitle(_translate("testMakingPage", "Frame"))
        self.testNameInput.setPlaceholderText(_translate("testMakingPage", "Input test name"))
        self.testDescriptionInput.setPlaceholderText(_translate("testMakingPage", "Input test description"))
        self.testNameLabel.setText(_translate("testMakingPage", "Test Name"))
        self.addTaskButton.setText(_translate("testMakingPage", "  Add Task  "))
        self.finishButton.setText(_translate("testMakingPage", "  Finish  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testMakingPage = QtWidgets.QFrame()
    ui = Ui_testMakingPage()
    ui.setupUi(testMakingPage)
    testMakingPage.show()
    sys.exit(app.exec_())
