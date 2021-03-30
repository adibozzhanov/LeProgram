# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/askLepPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_askLepPage(object):
    def setupUi(self, askLepPage):
        askLepPage.setObjectName("askLepPage")
        askLepPage.resize(1488, 712)
        askLepPage.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);")
        self.gridLayout = QtWidgets.QGridLayout(askLepPage)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(askLepPage)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.expressionInput = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expressionInput.sizePolicy().hasHeightForWidth())
        self.expressionInput.setSizePolicy(sizePolicy)
        self.expressionInput.setMinimumSize(QtCore.QSize(450, 68))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.expressionInput.setFont(font)
        self.expressionInput.setObjectName("expressionInput")
        self.horizontalLayout_5.addWidget(self.expressionInput)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 68))
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_5.addWidget(self.searchButton)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.EnterExpressionLabel = QtWidgets.QLabel(askLepPage)
        self.EnterExpressionLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.EnterExpressionLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.EnterExpressionLabel.setFont(font)
        self.EnterExpressionLabel.setObjectName("EnterExpressionLabel")
        self.gridLayout.addWidget(self.EnterExpressionLabel, 0, 1, 1, 1)
        self.askLepTabWidget = QtWidgets.QTabWidget(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepTabWidget.sizePolicy().hasHeightForWidth())
        self.askLepTabWidget.setSizePolicy(sizePolicy)
        self.askLepTabWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.askLepTabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.askLepTabWidget.setStyleSheet("border-color: rgb(246, 247, 200);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(246, 247, 200);")
        self.askLepTabWidget.setObjectName("askLepTabWidget")
        self.howToTab = QtWidgets.QWidget()
        self.howToTab.setObjectName("howToTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.howToTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.howToTextBox = QtWidgets.QTextEdit(self.howToTab)
        self.howToTextBox.setEnabled(False)
        self.howToTextBox.setObjectName("howToTextBox")
        self.horizontalLayout.addWidget(self.howToTextBox)
        self.askLepTabWidget.addTab(self.howToTab, "")
        self.cheatSheetTab = QtWidgets.QWidget()
        self.cheatSheetTab.setObjectName("cheatSheetTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cheatSheetTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cheatSheetTextBox = QtWidgets.QLabel(self.cheatSheetTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cheatSheetTextBox.sizePolicy().hasHeightForWidth())
        self.cheatSheetTextBox.setSizePolicy(sizePolicy)
        self.cheatSheetTextBox.setMinimumSize(QtCore.QSize(200, 500))
        self.cheatSheetTextBox.setMaximumSize(QtCore.QSize(1500, 800))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.cheatSheetTextBox.setFont(font)
        self.cheatSheetTextBox.setObjectName("cheatSheetTextBox")
        self.gridLayout_3.addWidget(self.cheatSheetTextBox, 0, 0, 1, 1)
        self.askLepTabWidget.addTab(self.cheatSheetTab, "")
        self.myNotesTab = QtWidgets.QWidget()
        self.myNotesTab.setObjectName("myNotesTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.myNotesTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.myNotesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.askLepTabWidget.addTab(self.myNotesTab, "")
        self.gridLayout.addWidget(self.askLepTabWidget, 2, 1, 1, 1)
        self.askLepWidgetFrame = QtWidgets.QFrame(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepWidgetFrame.sizePolicy().hasHeightForWidth())
        self.askLepWidgetFrame.setSizePolicy(sizePolicy)
        self.askLepWidgetFrame.setMinimumSize(QtCore.QSize(100, 400))
        self.askLepWidgetFrame.setMaximumSize(QtCore.QSize(900, 16777215))
        self.askLepWidgetFrame.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"")
        self.askLepWidgetFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.askLepWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepWidgetFrame.setLineWidth(2)
        self.askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        self.askLepLayout = QtWidgets.QHBoxLayout(self.askLepWidgetFrame)
        self.askLepLayout.setObjectName("askLepLayout")
        self.gridLayout.addWidget(self.askLepWidgetFrame, 1, 3, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        self.retranslateUi(askLepPage)
        self.askLepTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(askLepPage)

    def retranslateUi(self, askLepPage):
        _translate = QtCore.QCoreApplication.translate
        askLepPage.setWindowTitle(_translate("askLepPage", "Frame"))
        self.searchButton.setText(_translate("askLepPage", "Search"))
        self.EnterExpressionLabel.setText(_translate("askLepPage", "Enter the Expression"))
        self.howToTextBox.setHtml(_translate("askLepPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">How to use AskLep: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1) Variables are single English alphabet ,can be upper or lower case.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2) Brackets () are used to alter precedence</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3) Type the expression in the box above and press search </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Logical Expressions:</span></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Operator</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Char Form</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Maths form</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">CS form</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">AND</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">and</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">∧</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&amp;&amp;</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">OR</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">or</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">∨</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">|</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">XOR</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">xor</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">⊕</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">!=</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">IMP</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">imp</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">→</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">=&gt;</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">IFF</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">iff</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">↔</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">==</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">TOP</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">top</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">⊤</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">True</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">BOT</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">bot</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">⊥</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">False</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NOT</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">not</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">¬</span></p></td>\n"
"<td style=\" border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">!</span></p></td></tr>\n"
"<tr>\n"
"<td></td>\n"
"<td></td>\n"
"<td></td>\n"
"<td></td></tr></table>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">For every operator, users are allowed to use any form they choose. </span></p></body></html>"))
        self.askLepTabWidget.setTabText(self.askLepTabWidget.indexOf(self.howToTab), _translate("askLepPage", "How To"))
        self.cheatSheetTextBox.setText(_translate("askLepPage", "Double negation law\n"
"¬¬P ≡ P\n"
"Commutative laws\n"
"P ∧ Q ≡ Q ∧ P\n"
"P ∨ Q ≡ Q ∨ P\n"
"Associative laws\n"
"P ∧ (Q ∧ R) ≡ (P ∧ Q) ∧ R\n"
"P ∨ (Q ∨ R) ≡ (P ∨ Q) ∨ R\n"
"Idempotent laws\n"
"P ∧ P ≡ P\n"
"P ∨ P ≡ P\n"
"Distributive laws\n"
"P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)\n"
"P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)\n"
"DeMorgan’s laws\n"
"¬(P ∧ Q) ≡ ¬P ∨ ¬Q\n"
"¬(P ∨ Q) ≡ ¬P ∧ ¬Q\n"
"Conditional laws\n"
"P ⇒ Q ≡ ¬P ∨ Q\n"
"P ⇒ Q ≡ ¬(P ∧ ¬Q)\n"
"Biconditional law\n"
"P ⇔ Q ≡ (P ⇒ Q) ∧ (Q ⇒ P)\n"
"Contrapositive law\n"
"P ⇒ Q ≡ ¬Q ⇒ ¬P\n"
"Tautology laws\n"
"P ∧ (a tautalogy) ≡ P\n"
"P ∨ (a tautology) is a tautology\n"
"¬(a tautology) is a contradiction\n"
"Contradiction laws\n"
"P ∧ (a contradiction) is a contradiction\n"
"P ∨ (a contradiction) ≡ P\n"
"¬(a contradiction) is a tautology\n"
"Quantifier negation laws\n"
"¬∃x s.t. P ≡ ∀x, ¬P\n"
"¬∀x, P ≡ ∃x s.t. P"))
        self.askLepTabWidget.setTabText(self.askLepTabWidget.indexOf(self.cheatSheetTab), _translate("askLepPage", "Cheat Sheet"))
        self.textEdit.setPlaceholderText(_translate("askLepPage", "Type your notes here"))
        self.askLepTabWidget.setTabText(self.askLepTabWidget.indexOf(self.myNotesTab), _translate("askLepPage", "My Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askLepPage = QtWidgets.QFrame()
    ui = Ui_askLepPage()
    ui.setupUi(askLepPage)
    askLepPage.show()
    sys.exit(app.exec_())
