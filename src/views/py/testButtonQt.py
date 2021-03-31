# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/testButton.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testButtonFrame(object):
    def setupUi(self, testButtonFrame):
        testButtonFrame.setObjectName("testButtonFrame")
        testButtonFrame.resize(635, 70)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(testButtonFrame.sizePolicy().hasHeightForWidth())
        testButtonFrame.setSizePolicy(sizePolicy)
        testButtonFrame.setStyleSheet("background-color: rgb(23, 161, 145);\n"
"border-color: rgb(23, 161, 145);")
        testButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalLayout = QtWidgets.QHBoxLayout(testButtonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.testNameLabel = QtWidgets.QLabel(testButtonFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.testNameLabel.setObjectName("testNameLabel")
        self.horizontalLayout.addWidget(self.testNameLabel)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem1)
        self.viewButton = QtWidgets.QPushButton(testButtonFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        font.setItalic(False)
        self.viewButton.setFont(font)
        self.viewButton.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout.addWidget(self.viewButton)
        self.startButton = QtWidgets.QPushButton(testButtonFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        font.setItalic(False)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)

        self.retranslateUi(testButtonFrame)
        QtCore.QMetaObject.connectSlotsByName(testButtonFrame)

    def retranslateUi(self, testButtonFrame):
        _translate = QtCore.QCoreApplication.translate
        testButtonFrame.setWindowTitle(_translate("testButtonFrame", "Frame"))
        self.testNameLabel.setText(_translate("testButtonFrame", "TestName"))
        self.viewButton.setText(_translate("testButtonFrame", "View"))
        self.startButton.setText(_translate("testButtonFrame", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testButtonFrame = QtWidgets.QFrame()
    ui = Ui_testButtonFrame()
    ui.setupUi(testButtonFrame)
    testButtonFrame.show()
    sys.exit(app.exec_())
