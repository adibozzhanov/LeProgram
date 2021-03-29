# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/testMaking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testMakingPage(object):
    def setupUi(self, testMakingPage):
        testMakingPage.setObjectName("testMakingPage")
        testMakingPage.resize(702, 555)
        self.gridLayout = QtWidgets.QGridLayout(testMakingPage)
        self.gridLayout.setObjectName("gridLayout")
        self.testNameInput = QtWidgets.QPlainTextEdit(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testNameInput.sizePolicy().hasHeightForWidth())
        self.testNameInput.setSizePolicy(sizePolicy)
        self.testNameInput.setMinimumSize(QtCore.QSize(100, 0))
        self.testNameInput.setMaximumSize(QtCore.QSize(16777215, 40))
        self.testNameInput.setObjectName("testNameInput")
        self.gridLayout.addWidget(self.testNameInput, 2, 1, 1, 1)
        self.testNameLabel = QtWidgets.QLabel(testMakingPage)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.gridLayout.addWidget(self.testNameLabel, 1, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 3, 1, 1)
        self.finishButton = QtWidgets.QPushButton(testMakingPage)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.finishButton.setFont(font)
        self.finishButton.setObjectName("finishButton")
        self.gridLayout.addWidget(self.finishButton, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.addTaskButton = QtWidgets.QPushButton(testMakingPage)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.addTaskButton.setFont(font)
        self.addTaskButton.setObjectName("addTaskButton")
        self.gridLayout.addWidget(self.addTaskButton, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.taskMakingScrollArea = QtWidgets.QScrollArea(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskMakingScrollArea.sizePolicy().hasHeightForWidth())
        self.taskMakingScrollArea.setSizePolicy(sizePolicy)
        self.taskMakingScrollArea.setMinimumSize(QtCore.QSize(200, 200))
        self.taskMakingScrollArea.setWidgetResizable(True)
        self.taskMakingScrollArea.setObjectName("taskMakingScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 474, 198))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.taskScrollBarContents = QtWidgets.QVBoxLayout()
        self.taskScrollBarContents.setObjectName("taskScrollBarContents")
        self.verticalLayout_2.addLayout(self.taskScrollBarContents)
        self.taskMakingScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.taskMakingScrollArea, 6, 1, 1, 2)
        self.askLepWidgetFrame = QtWidgets.QFrame(testMakingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepWidgetFrame.sizePolicy().hasHeightForWidth())
        self.askLepWidgetFrame.setSizePolicy(sizePolicy)
        self.askLepWidgetFrame.setMinimumSize(QtCore.QSize(100, 400))
        self.askLepWidgetFrame.setMaximumSize(QtCore.QSize(900, 16777215))
        self.askLepWidgetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.askLepWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        self.gridLayout.addWidget(self.askLepWidgetFrame, 0, 4, 7, 1)
        self.testDescriptionInput = QtWidgets.QPlainTextEdit(testMakingPage)
        self.testDescriptionInput.setPlainText("")
        self.testDescriptionInput.setObjectName("testDescriptionInput")
        self.gridLayout.addWidget(self.testDescriptionInput, 3, 1, 1, 1)

        self.retranslateUi(testMakingPage)
        QtCore.QMetaObject.connectSlotsByName(testMakingPage)

    def retranslateUi(self, testMakingPage):
        _translate = QtCore.QCoreApplication.translate
        testMakingPage.setWindowTitle(_translate("testMakingPage", "Frame"))
        self.testNameInput.setPlaceholderText(_translate("testMakingPage", "Input your Test Name here"))
        self.testNameLabel.setText(_translate("testMakingPage", "Test Name"))
        self.finishButton.setText(_translate("testMakingPage", "Finish"))
        self.addTaskButton.setText(_translate("testMakingPage", "Add Task"))
        self.testDescriptionInput.setPlaceholderText(_translate("testMakingPage", "Input your test description here "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testMakingPage = QtWidgets.QFrame()
    ui = Ui_testMakingPage()
    ui.setupUi(testMakingPage)
    testMakingPage.show()
    sys.exit(app.exec_())
