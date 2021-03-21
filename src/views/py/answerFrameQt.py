# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/answerFrame.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_answerFrame(object):
    def setupUi(self, answerFrame):
        answerFrame.setObjectName("answerFrame")
        answerFrame.resize(516, 71)
        self.horizontalLayout = QtWidgets.QHBoxLayout(answerFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.answerButton = QtWidgets.QPushButton(answerFrame)
        self.answerButton.setObjectName("answerButton")
        self.horizontalLayout.addWidget(self.answerButton)

        self.retranslateUi(answerFrame)
        QtCore.QMetaObject.connectSlotsByName(answerFrame)

    def retranslateUi(self, answerFrame):
        _translate = QtCore.QCoreApplication.translate
        answerFrame.setWindowTitle(_translate("answerFrame", "Frame"))
        self.answerButton.setText(_translate("answerFrame", "Answer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    answerFrame = QtWidgets.QFrame()
    ui = Ui_answerFrame()
    ui.setupUi(answerFrame)
    answerFrame.show()
    sys.exit(app.exec_())
