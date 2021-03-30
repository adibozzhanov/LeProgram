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
        answerInputFrame.resize(828, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(answerInputFrame.sizePolicy().hasHeightForWidth())
        answerInputFrame.setSizePolicy(sizePolicy)
        answerInputFrame.setMinimumSize(QtCore.QSize(0, 0))
        answerInputFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(answerInputFrame)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.answerInputField = QtWidgets.QPlainTextEdit(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerInputField.sizePolicy().hasHeightForWidth())
        self.answerInputField.setSizePolicy(sizePolicy)
        self.answerInputField.setMinimumSize(QtCore.QSize(500, 60))
        self.answerInputField.setMaximumSize(QtCore.QSize(4000, 75))
        self.answerInputField.setObjectName("answerInputField")
        self.gridLayout.addWidget(self.answerInputField, 0, 1, 1, 1)
        self.ifCorrectCheckBox = QtWidgets.QCheckBox(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ifCorrectCheckBox.sizePolicy().hasHeightForWidth())
        self.ifCorrectCheckBox.setSizePolicy(sizePolicy)
        self.ifCorrectCheckBox.setMinimumSize(QtCore.QSize(90, 50))
        self.ifCorrectCheckBox.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifCorrectCheckBox.setFont(font)
        self.ifCorrectCheckBox.setObjectName("ifCorrectCheckBox")
        self.gridLayout.addWidget(self.ifCorrectCheckBox, 0, 4, 1, 1)
        self.ifValidLabel = QtWidgets.QLabel(answerInputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ifValidLabel.sizePolicy().hasHeightForWidth())
        self.ifValidLabel.setSizePolicy(sizePolicy)
        self.ifValidLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.ifValidLabel.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifValidLabel.setFont(font)
        self.ifValidLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.ifValidLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ifValidLabel.setObjectName("ifValidLabel")
        self.gridLayout.addWidget(self.ifValidLabel, 0, 0, 1, 1)

        self.retranslateUi(answerInputFrame)
        QtCore.QMetaObject.connectSlotsByName(answerInputFrame)

    def retranslateUi(self, answerInputFrame):
        _translate = QtCore.QCoreApplication.translate
        answerInputFrame.setWindowTitle(_translate("answerInputFrame", "Frame"))
        self.answerInputField.setPlaceholderText(_translate("answerInputFrame", "Write answer here"))
        self.ifCorrectCheckBox.setText(_translate("answerInputFrame", "Correct"))
        self.ifValidLabel.setText(_translate("answerInputFrame", "Invalid"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    answerInputFrame = QtWidgets.QFrame()
    ui = Ui_answerInputFrame()
    ui.setupUi(answerInputFrame)
    answerInputFrame.show()
    sys.exit(app.exec_())
