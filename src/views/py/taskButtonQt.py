# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/taskButton.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskFrame(object):
    def setupUi(self, taskFrame):
        taskFrame.setObjectName("taskFrame")
        taskFrame.resize(677, 80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(taskFrame.sizePolicy().hasHeightForWidth())
        taskFrame.setSizePolicy(sizePolicy)
        taskFrame.setMinimumSize(QtCore.QSize(0, 80))
        taskFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        taskFrame.setStyleSheet("background-color: rgb(23, 161, 145);\n"
"color: rgb(255, 255, 255);")
        taskFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalLayout = QtWidgets.QHBoxLayout(taskFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taskNameLabel = QtWidgets.QLabel(taskFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout.addWidget(self.taskNameLabel)
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem1)
        self.viewButton = QtWidgets.QPushButton(taskFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        font.setItalic(False)
        self.viewButton.setFont(font)
        self.viewButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout.addWidget(self.viewButton)

        self.retranslateUi(taskFrame)
        QtCore.QMetaObject.connectSlotsByName(taskFrame)

    def retranslateUi(self, taskFrame):
        _translate = QtCore.QCoreApplication.translate
        taskFrame.setWindowTitle(_translate("taskFrame", "Frame"))
        self.taskNameLabel.setText(_translate("taskFrame", "Sample question"))
        self.viewButton.setText(_translate("taskFrame", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    taskFrame = QtWidgets.QFrame()
    ui = Ui_taskFrame()
    ui.setupUi(taskFrame)
    taskFrame.show()
    sys.exit(app.exec_())
