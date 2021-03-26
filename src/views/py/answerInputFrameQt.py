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
        answerInputFrame.resize(754, 68)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(answerInputFrame.sizePolicy().hasHeightForWidth())
        answerInputFrame.setSizePolicy(sizePolicy)
        answerInputFrame.setMinimumSize(QtCore.QSize(0, 50))
        answerInputFrame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.gridLayout = QtWidgets.QGridLayout(answerInputFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.answerInputField = QtWidgets.QPlainTextEdit(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerInputField.sizePolicy().hasHeightForWidth())
        self.answerInputField.setSizePolicy(sizePolicy)
        self.answerInputField.setMinimumSize(QtCore.QSize(500, 68))
        self.answerInputField.setMaximumSize(QtCore.QSize(800, 50))
        self.answerInputField.setObjectName("answerInputField")
        self.gridLayout.addWidget(self.answerInputField, 0, 1, 1, 1)
        self.ifCorrectCheckBox = QtWidgets.QCheckBox(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ifCorrectCheckBox.sizePolicy().hasHeightForWidth())
        self.ifCorrectCheckBox.setSizePolicy(sizePolicy)
        self.ifCorrectCheckBox.setMinimumSize(QtCore.QSize(90, 68))
        self.ifCorrectCheckBox.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifCorrectCheckBox.setFont(font)
        self.ifCorrectCheckBox.setObjectName("ifCorrectCheckBox")
        self.gridLayout.addWidget(self.ifCorrectCheckBox, 0, 3, 1, 1)
        self.ifValidLabel = QtWidgets.QLabel(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ifValidLabel.sizePolicy().hasHeightForWidth())
        self.ifValidLabel.setSizePolicy(sizePolicy)
        self.ifValidLabel.setMinimumSize(QtCore.QSize(200, 68))
        self.ifValidLabel.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifValidLabel.setFont(font)
        self.ifValidLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.ifValidLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ifValidLabel.setObjectName("ifValidLabel")
        self.gridLayout.addWidget(self.ifValidLabel, 0, 2, 1, 1)

        self.retranslateUi(answerInputFrame)
        QtCore.QMetaObject.connectSlotsByName(answerInputFrame)

    def retranslateUi(self, answerInputFrame):
        _translate = QtCore.QCoreApplication.translate
        answerInputFrame.setWindowTitle(_translate("answerInputFrame", "Frame"))
        self.answerInputField.setPlaceholderText(_translate("answerInputFrame", "Write answer here"))
        self.ifCorrectCheckBox.setText(_translate("answerInputFrame", "Correct"))
        self.ifValidLabel.setText(_translate("answerInputFrame", "Invalid Expression"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    answerInputFrame = QtWidgets.QFrame()
    ui = Ui_answerInputFrame()
    ui.setupUi(answerInputFrame)
    answerInputFrame.show()
    sys.exit(app.exec_())
