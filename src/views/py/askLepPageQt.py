# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/askLepPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_askLepPage(object):
    def setupUi(self, askLepPage):
        askLepPage.setObjectName("askLepPage")
        askLepPage.resize(1116, 740)
        self.gridLayout = QtWidgets.QGridLayout(askLepPage)
        self.gridLayout.setObjectName("gridLayout")
        self.EnterExpressionLabel = QtWidgets.QLabel(askLepPage)
        self.EnterExpressionLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.EnterExpressionLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.EnterExpressionLabel.setFont(font)
        self.EnterExpressionLabel.setObjectName("EnterExpressionLabel")
        self.gridLayout.addWidget(self.EnterExpressionLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.frame = QtWidgets.QFrame(askLepPage)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.expressionInput = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expressionInput.sizePolicy().hasHeightForWidth())
        self.expressionInput.setSizePolicy(sizePolicy)
        self.expressionInput.setMinimumSize(QtCore.QSize(600, 50))
        self.expressionInput.setMaximumSize(QtCore.QSize(16777215, 100))
        self.expressionInput.setObjectName("expressionInput")
        self.horizontalLayout_5.addWidget(self.expressionInput)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setMinimumSize(QtCore.QSize(60, 0))
        self.searchButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_5.addWidget(self.searchButton)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.askLepWidgetFrame = QtWidgets.QFrame(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepWidgetFrame.sizePolicy().hasHeightForWidth())
        self.askLepWidgetFrame.setSizePolicy(sizePolicy)
        self.askLepWidgetFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.askLepWidgetFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.askLepWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        self.askLepLayout = QtWidgets.QHBoxLayout(self.askLepWidgetFrame)
        self.askLepLayout.setObjectName("askLepLayout")
        self.gridLayout.addWidget(self.askLepWidgetFrame, 2, 1, 2, 1)
        self.askLepTabWidget = QtWidgets.QTabWidget(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepTabWidget.sizePolicy().hasHeightForWidth())
        self.askLepTabWidget.setSizePolicy(sizePolicy)
        self.askLepTabWidget.setMinimumSize(QtCore.QSize(400, 200))
        self.askLepTabWidget.setObjectName("askLepTabWidget")
        self.howToTab = QtWidgets.QWidget()
        self.howToTab.setObjectName("howToTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.howToTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.howToScrollArea = QtWidgets.QScrollArea(self.howToTab)
        self.howToScrollArea.setWidgetResizable(True)
        self.howToScrollArea.setObjectName("howToScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(-72, -38, 711, 537))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.howToTextBox = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.howToTextBox.sizePolicy().hasHeightForWidth())
        self.howToTextBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.howToTextBox.setFont(font)
        self.howToTextBox.setObjectName("howToTextBox")
        self.horizontalLayout_2.addWidget(self.howToTextBox)
        self.howToScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.addWidget(self.howToScrollArea)
        self.askLepTabWidget.addTab(self.howToTab, "")
        self.cheatSheetTab = QtWidgets.QWidget()
        self.cheatSheetTab.setObjectName("cheatSheetTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cheatSheetTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cheatSheetScrollArea = QtWidgets.QScrollArea(self.cheatSheetTab)
        self.cheatSheetScrollArea.setWidgetResizable(True)
        self.cheatSheetScrollArea.setObjectName("cheatSheetScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 660, 520))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cheatSheetTextBox = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cheatSheetTextBox.sizePolicy().hasHeightForWidth())
        self.cheatSheetTextBox.setSizePolicy(sizePolicy)
        self.cheatSheetTextBox.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cheatSheetTextBox.setFont(font)
        self.cheatSheetTextBox.setObjectName("cheatSheetTextBox")
        self.horizontalLayout_3.addWidget(self.cheatSheetTextBox)
        self.cheatSheetScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.cheatSheetScrollArea, 0, 0, 1, 1)
        self.askLepTabWidget.addTab(self.cheatSheetTab, "")
        self.myNotesTab = QtWidgets.QWidget()
        self.myNotesTab.setObjectName("myNotesTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.myNotesTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.askLepTabWidget.addTab(self.myNotesTab, "")
        self.gridLayout.addWidget(self.askLepTabWidget, 3, 0, 1, 1)

        self.retranslateUi(askLepPage)
        self.askLepTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(askLepPage)

    def retranslateUi(self, askLepPage):
        _translate = QtCore.QCoreApplication.translate
        askLepPage.setWindowTitle(_translate("askLepPage", "Frame"))
        self.EnterExpressionLabel.setText(_translate("askLepPage", "Enter the Expression"))
        self.searchButton.setText(_translate("askLepPage", "search"))
        self.howToTextBox.setText(_translate("askLepPage", "<html>\n"
"<head>\n"
"<style>\n"
"table, th, td {\n"
"  border: 1px solid black;\n"
"  border-collapse: collapse;\n"
"}\n"
"</style>\n"
"</head>\n"
"        <body><p>How to use AskLep:</p>\n"
"        <p>1) Variables are single English alphabet ,can be upper or lower case.</p>\n"
"<p>2) Brackets () are used to alter precedence</p>\n"
"<p>3) Type the expression in the box above and press search</p>\n"
"        <p>Logical Expressions:</p>\n"
"<table>\n"
"  <tr>\n"
"    <th>Operator</th>\n"
"    <th>Char Form</th>\n"
"    <th>Maths form</th>\n"
"    <th>CS form</th>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>AND</td>\n"
"    <td>and</td>\n"
"    <td>∧</td>\n"
"    <td>&&</td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>OR</td>\n"
"    <td>or</td>\n"
"    <td>∨</td>\n"
"    <td>|</td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>XOR</td>\n"
"    <td>xor</td>\n"
"    <td>⊕</td>\n"
"    <td>!=</td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>IMP</td>\n"
"    <td>imp</td>\n"
"    <td>→</td>\n"
"    <td>=></td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>IFF</td>\n"
"    <td>iff</td>\n"
"    <td>↔</td>\n"
"    <td>==</td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>TOP</td>\n"
"    <td>top</td>\n"
"    <td>⊤</td>\n"
"    <td>True</td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>BOT</td>\n"
"    <td>bot</td>\n"
"    <td>⊥</td>\n"
"    <td>False</td>\n"
"  </tr>\n"
"  <tr>\n"
"    <td>NOT</td>\n"
"    <td>not</td>\n"
"    <td>¬</td>\n"
"    <td>!</td>\n"
"  </tr>\n"
"  <tr>\n"
"</table>\n"
"        <p>For every operator, users are allowed to use any form they choose.</p>\n"
"\n"
"        </body>\n"
"</html>"))
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
        self.askLepTabWidget.setTabText(self.askLepTabWidget.indexOf(self.myNotesTab), _translate("askLepPage", "My Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askLepPage = QtWidgets.QFrame()
    ui = Ui_askLepPage()
    ui.setupUi(askLepPage)
    askLepPage.show()
    sys.exit(app.exec_())
