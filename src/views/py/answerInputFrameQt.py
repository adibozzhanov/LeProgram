# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/answerInputFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_answerInputFrame(object):
    def setupUi(self, answerInputFrame):
        answerInputFrame.setObjectName("answerInputFrame")
        answerInputFrame.resize(646, 68)
        answerInputFrame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.verticalLayout = QtWidgets.QVBoxLayout(answerInputFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.answerInputField = QtWidgets.QPlainTextEdit(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerInputField.sizePolicy().hasHeightForWidth())
        self.answerInputField.setSizePolicy(sizePolicy)
        self.answerInputField.setMinimumSize(QtCore.QSize(0, 0))
        self.answerInputField.setMaximumSize(QtCore.QSize(16777215, 50))
        self.answerInputField.setObjectName("answerInputField")
        self.verticalLayout.addWidget(self.answerInputField)

        self.retranslateUi(answerInputFrame)
        QtCore.QMetaObject.connectSlotsByName(answerInputFrame)

    def retranslateUi(self, answerInputFrame):
        _translate = QtCore.QCoreApplication.translate
        answerInputFrame.setWindowTitle(_translate("answerInputFrame", "Frame"))
        self.answerInputField.setPlaceholderText(_translate("answerInputFrame", "Write answer here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    answerInputFrame = QtWidgets.QFrame()
    ui = Ui_answerInputFrame()
    ui.setupUi(answerInputFrame)
    answerInputFrame.show()
    sys.exit(app.exec_())