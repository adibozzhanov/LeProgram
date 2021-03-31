# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/taskFrame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskFrame(object):
    def setupUi(self, taskFrame):
        taskFrame.setObjectName("taskFrame")
        taskFrame.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(taskFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.taskStatementLabel = QtWidgets.QLabel(taskFrame)
        self.taskStatementLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.taskStatementLabel.setWordWrap(True)
        self.taskStatementLabel.setObjectName("taskStatementLabel")
        self.verticalLayout.addWidget(self.taskStatementLabel)
        self.expressionLabel = QtWidgets.QLabel(taskFrame)
        self.expressionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.expressionLabel.setWordWrap(True)
        self.expressionLabel.setObjectName("expressionLabel")
        self.verticalLayout.addWidget(self.expressionLabel)
        self.answersFrame = QtWidgets.QFrame(taskFrame)
        self.answersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answersFrame.setObjectName("answersFrame")
        self.answersLayout = QtWidgets.QVBoxLayout(self.answersFrame)
        self.answersLayout.setObjectName("answersLayout")
        self.verticalLayout.addWidget(self.answersFrame)

        self.retranslateUi(taskFrame)
        QtCore.QMetaObject.connectSlotsByName(taskFrame)

    def retranslateUi(self, taskFrame):
        _translate = QtCore.QCoreApplication.translate
        taskFrame.setWindowTitle(_translate("taskFrame", "Frame"))
        self.taskStatementLabel.setText(_translate("taskFrame", "Task Statement"))
        self.expressionLabel.setText(_translate("taskFrame", "expresion Label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    taskFrame = QtWidgets.QFrame()
    ui = Ui_taskFrame()
    ui.setupUi(taskFrame)
    taskFrame.show()
    sys.exit(app.exec_())
