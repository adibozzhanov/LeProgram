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
        self.gridLayout = QtWidgets.QGridLayout(randomQuestionFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(randomQuestionFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(randomQuestionFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.descriptionLabel = QtWidgets.QTextBrowser(randomQuestionFrame)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 3, 0, 1, 1)
        self.radioFrame = QtWidgets.QFrame(randomQuestionFrame)
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
        self.gridLayout.addWidget(self.radioFrame, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.frame = QtWidgets.QFrame(randomQuestionFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(randomQuestionFrame)
        QtCore.QMetaObject.connectSlotsByName(randomQuestionFrame)

    def retranslateUi(self, randomQuestionFrame):
        _translate = QtCore.QCoreApplication.translate
        randomQuestionFrame.setWindowTitle(_translate("randomQuestionFrame", "Frame"))
        self.label.setText(_translate("randomQuestionFrame", "Please select the complexity of questions."))
        self.titleLabel.setText(_translate("randomQuestionFrame", "Random Question Generator"))
        self.descriptionLabel.setHtml(_translate("randomQuestionFrame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Sans Semi-Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some description of what is a random question generator</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.radioButton_3.setText(_translate("randomQuestionFrame", "1"))
        self.radioButton_6.setText(_translate("randomQuestionFrame", "2"))
        self.radioButton_5.setText(_translate("randomQuestionFrame", "3"))
        self.radioButton_4.setText(_translate("randomQuestionFrame", "4"))
        self.radioButton.setText(_translate("randomQuestionFrame", "5"))
        self.radioButton_2.setText(_translate("randomQuestionFrame", "6"))
        self.pushButton.setText(_translate("randomQuestionFrame", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    randomQuestionFrame = QtWidgets.QFrame()
    ui = Ui_randomQuestionFrame()
    ui.setupUi(randomQuestionFrame)
    randomQuestionFrame.show()
    sys.exit(app.exec_())
