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
        testButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalLayout = QtWidgets.QHBoxLayout(testButtonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.testNameLabel = QtWidgets.QLabel(testButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.horizontalLayout.addWidget(self.testNameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.viewButton = QtWidgets.QPushButton(testButtonFrame)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout.addWidget(self.viewButton)
        self.startButton = QtWidgets.QPushButton(testButtonFrame)
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