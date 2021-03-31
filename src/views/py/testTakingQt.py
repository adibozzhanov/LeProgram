# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/testTaking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testTakingFrame(object):
    def setupUi(self, testTakingFrame):
        testTakingFrame.setObjectName("testTakingFrame")
        testTakingFrame.resize(763, 564)
        testTakingFrame.setStyleSheet("background-color: rgb(255, 255, 242);")
        self.mainLayout = QtWidgets.QHBoxLayout(testTakingFrame)
        self.mainLayout.setObjectName("mainLayout")
        spacerItem = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(testTakingFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.testNameLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        font.setItalic(True)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout_2.addWidget(self.testNameLabel)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    text-align : center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 161, 145);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.taskFrame = QtWidgets.QFrame(self.frame)
        self.taskFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taskFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskFrame.setObjectName("taskFrame")
        self.taskLayout = QtWidgets.QHBoxLayout(self.taskFrame)
        self.taskLayout.setObjectName("taskLayout")
        self.verticalLayout_2.addWidget(self.taskFrame)
        self.nextQButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setItalic(True)
        self.nextQButton.setFont(font)
        self.nextQButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.nextQButton.setObjectName("nextQButton")
        self.verticalLayout_2.addWidget(self.nextQButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.mainLayout.addWidget(self.frame)
        self.askLepFrame = QtWidgets.QFrame(testTakingFrame)
        self.askLepFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.askLepFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.askLepFrame.setObjectName("askLepFrame")
        self.askLepLayout = QtWidgets.QHBoxLayout(self.askLepFrame)
        self.askLepLayout.setObjectName("askLepLayout")
        self.mainLayout.addWidget(self.askLepFrame)
        spacerItem2 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem2)

        self.retranslateUi(testTakingFrame)
        QtCore.QMetaObject.connectSlotsByName(testTakingFrame)

    def retranslateUi(self, testTakingFrame):
        _translate = QtCore.QCoreApplication.translate
        testTakingFrame.setWindowTitle(_translate("testTakingFrame", "Frame"))
        self.testNameLabel.setText(_translate("testTakingFrame", "Test Name"))
        self.nextQButton.setText(_translate("testTakingFrame", "Next Question"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testTakingFrame = QtWidgets.QFrame()
    ui = Ui_testTakingFrame()
    ui.setupUi(testTakingFrame)
    testTakingFrame.show()
    sys.exit(app.exec_())
