# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/randomPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_randomQuestionFrame(object):
    def setupUi(self, randomQuestionFrame):
        randomQuestionFrame.setObjectName("randomQuestionFrame")
        randomQuestionFrame.resize(649, 523)
        randomQuestionFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        randomQuestionFrame.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);")
        self.gridLayout = QtWidgets.QGridLayout(randomQuestionFrame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.radioFrame = QtWidgets.QFrame(randomQuestionFrame)
        self.radioFrame.setStyleSheet("background-color: rgb(23, 161, 145);\n"
"color: rgb(255, 255, 255);")
        self.radioFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.radioFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.radioFrame.setObjectName("radioFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.radioFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.radioFrame)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_6 = QtWidgets.QRadioButton(self.radioFrame)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout.addWidget(self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.radioFrame)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.radioFrame)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.radioFrame)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.radioFrame)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.gridLayout.addWidget(self.radioFrame, 5, 1, 1, 1)
        self.descriptionLabel = QtWidgets.QTextBrowser(randomQuestionFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setStyleSheet("background-color: rgb(246, 247, 200);")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(randomQuestionFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)
        self.titleLabel = QtWidgets.QLabel(randomQuestionFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.frame = QtWidgets.QFrame(randomQuestionFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.startButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        font.setItalic(True)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)

        self.retranslateUi(randomQuestionFrame)
        QtCore.QMetaObject.connectSlotsByName(randomQuestionFrame)

    def retranslateUi(self, randomQuestionFrame):
        _translate = QtCore.QCoreApplication.translate
        randomQuestionFrame.setWindowTitle(_translate("randomQuestionFrame", "Frame"))
        self.radioButton_3.setText(_translate("randomQuestionFrame", "1"))
        self.radioButton_6.setText(_translate("randomQuestionFrame", "2"))
        self.radioButton_5.setText(_translate("randomQuestionFrame", "3"))
        self.radioButton_4.setText(_translate("randomQuestionFrame", "4"))
        self.radioButton.setText(_translate("randomQuestionFrame", "5"))
        self.radioButton_2.setText(_translate("randomQuestionFrame", "6"))
        self.descriptionLabel.setHtml(_translate("randomQuestionFrame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Fira Sans Semi-Light\';\">A random question generator generates questions randomly. When you select a higher complexity, you get a problem that is more complex.</span></p></body></html>"))
        self.label.setText(_translate("randomQuestionFrame", "Please select the complexity of questions."))
        self.titleLabel.setText(_translate("randomQuestionFrame", "Random Question Generator"))
        self.startButton.setText(_translate("randomQuestionFrame", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    randomQuestionFrame = QtWidgets.QFrame()
    ui = Ui_randomQuestionFrame()
    ui.setupUi(randomQuestionFrame)
    randomQuestionFrame.show()
    sys.exit(app.exec_())
