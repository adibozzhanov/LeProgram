# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/testResultFrame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testResultFrame(object):
    def setupUi(self, testResultFrame):
        testResultFrame.setObjectName("testResultFrame")
        testResultFrame.resize(618, 549)
        self.verticalLayout = QtWidgets.QVBoxLayout(testResultFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testNameLabel = QtWidgets.QLabel(testResultFrame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout.addWidget(self.testNameLabel)
        self.scoreLabel = QtWidgets.QLabel(testResultFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.verticalLayout.addWidget(self.scoreLabel)

        self.retranslateUi(testResultFrame)
        QtCore.QMetaObject.connectSlotsByName(testResultFrame)

    def retranslateUi(self, testResultFrame):
        _translate = QtCore.QCoreApplication.translate
        testResultFrame.setWindowTitle(_translate("testResultFrame", "Frame"))
        self.testNameLabel.setText(_translate("testResultFrame", "TestName"))
        self.scoreLabel.setText(_translate("testResultFrame", "Score Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testResultFrame = QtWidgets.QFrame()
    ui = Ui_testResultFrame()
    ui.setupUi(testResultFrame)
    testResultFrame.show()
    sys.exit(app.exec_())
