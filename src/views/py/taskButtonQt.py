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
        taskFrame.resize(438, 43)
        taskFrame.setMinimumSize(QtCore.QSize(0, 40))
        taskFrame.setMaximumSize(QtCore.QSize(16777215, 43))
        taskFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalLayout = QtWidgets.QHBoxLayout(taskFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taskNameLabel = QtWidgets.QLabel(taskFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout.addWidget(self.taskNameLabel)
        spacerItem = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.viewButton = QtWidgets.QPushButton(taskFrame)
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
