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
        self.verticalLayout = QtWidgets.QVBoxLayout(testTakingFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testNameLabel = QtWidgets.QLabel(testTakingFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout.addWidget(self.testNameLabel)
        self.progressBar = QtWidgets.QProgressBar(testTakingFrame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.taskFrame = QtWidgets.QFrame(testTakingFrame)
        self.taskFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.taskFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskFrame.setObjectName("taskFrame")
        self.taskLayout = QtWidgets.QHBoxLayout(self.taskFrame)
        self.taskLayout.setObjectName("taskLayout")
        self.verticalLayout.addWidget(self.taskFrame)
        self.nextQButton = QtWidgets.QPushButton(testTakingFrame)
        self.nextQButton.setObjectName("nextQButton")
        self.verticalLayout.addWidget(self.nextQButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

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
