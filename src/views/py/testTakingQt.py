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
        self.askLepLayout = QtWidgets.QHBoxLayout(testTakingFrame)
        self.askLepLayout.setObjectName("askLepLayout")
        self.frame = QtWidgets.QFrame(testTakingFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.testNameLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout_2.addWidget(self.testNameLabel)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.taskFrame = QtWidgets.QFrame(self.frame)
        self.taskFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.taskFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskFrame.setObjectName("taskFrame")
        self.taskLayout = QtWidgets.QHBoxLayout(self.taskFrame)
        self.taskLayout.setObjectName("taskLayout")
        self.verticalLayout_2.addWidget(self.taskFrame)
        self.nextQButton = QtWidgets.QPushButton(self.frame)
        self.nextQButton.setObjectName("nextQButton")
        self.verticalLayout_2.addWidget(self.nextQButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.askLepLayout.addWidget(self.frame)
        self.askLepFrame = QtWidgets.QFrame(testTakingFrame)
        self.askLepFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.askLepFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepFrame.setObjectName("askLepFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.askLepFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.askLepLayout.addWidget(self.askLepFrame)

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
