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
        askLepPage.resize(1316, 756)
        self.gridLayout = QtWidgets.QGridLayout(askLepPage)
        self.gridLayout.setObjectName("gridLayout")
        self.EnterExpressionLabel = QtWidgets.QLabel(askLepPage)
        self.EnterExpressionLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.EnterExpressionLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.EnterExpressionLabel.setFont(font)
        self.EnterExpressionLabel.setObjectName("EnterExpressionLabel")
        self.gridLayout.addWidget(self.EnterExpressionLabel, 0, 1, 1, 2)
        self.askLepWidgetFrame = QtWidgets.QFrame(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepWidgetFrame.sizePolicy().hasHeightForWidth())
        self.askLepWidgetFrame.setSizePolicy(sizePolicy)
        self.askLepWidgetFrame.setMinimumSize(QtCore.QSize(400, 400))
        self.askLepWidgetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.askLepWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        self.gridLayout.addWidget(self.askLepWidgetFrame, 1, 2, 3, 1)
        self.expressionInput = QtWidgets.QPlainTextEdit(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expressionInput.sizePolicy().hasHeightForWidth())
        self.expressionInput.setSizePolicy(sizePolicy)
        self.expressionInput.setMinimumSize(QtCore.QSize(600, 50))
        self.expressionInput.setMaximumSize(QtCore.QSize(16777215, 100))
        self.expressionInput.setObjectName("expressionInput")
        self.gridLayout.addWidget(self.expressionInput, 1, 1, 1, 1)
        self.askLepTabWidget = QtWidgets.QTabWidget(askLepPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepTabWidget.sizePolicy().hasHeightForWidth())
        self.askLepTabWidget.setSizePolicy(sizePolicy)
        self.askLepTabWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.askLepTabWidget.setObjectName("askLepTabWidget")
        self.howToTab = QtWidgets.QWidget()
        self.howToTab.setObjectName("howToTab")
        self.howToScrollArea = QtWidgets.QScrollArea(self.howToTab)
        self.howToScrollArea.setGeometry(QtCore.QRect(-1, 0, 801, 551))
        self.howToScrollArea.setWidgetResizable(True)
        self.howToScrollArea.setObjectName("howToScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 799, 549))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.howToTextBox = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.howToTextBox.setGeometry(QtCore.QRect(0, 0, 801, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.howToTextBox.sizePolicy().hasHeightForWidth())
        self.howToTextBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.howToTextBox.setFont(font)
        self.howToTextBox.setObjectName("howToTextBox")
        self.howToScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.askLepTabWidget.addTab(self.howToTab, "")
        self.cheatSheetTab = QtWidgets.QWidget()
        self.cheatSheetTab.setObjectName("cheatSheetTab")
        self.cheatSheetScrollArea = QtWidgets.QScrollArea(self.cheatSheetTab)
        self.cheatSheetScrollArea.setGeometry(QtCore.QRect(0, 0, 821, 571))
        self.cheatSheetScrollArea.setWidgetResizable(True)
        self.cheatSheetScrollArea.setObjectName("cheatSheetScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.cheatSheetTextBox = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.cheatSheetTextBox.setGeometry(QtCore.QRect(0, 0, 821, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cheatSheetTextBox.sizePolicy().hasHeightForWidth())
        self.cheatSheetTextBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cheatSheetTextBox.setFont(font)
        self.cheatSheetTextBox.setObjectName("cheatSheetTextBox")
        self.cheatSheetScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.askLepTabWidget.addTab(self.cheatSheetTab, "")
        self.myNotesTab = QtWidgets.QWidget()
        self.myNotesTab.setObjectName("myNotesTab")
        self.myNotesScrollArea = QtWidgets.QScrollArea(self.myNotesTab)
        self.myNotesScrollArea.setGeometry(QtCore.QRect(-1, 0, 911, 571))
        self.myNotesScrollArea.setWidgetResizable(True)
        self.myNotesScrollArea.setObjectName("myNotesScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 909, 569))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.myNotesTextInput = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.myNotesTextInput.setGeometry(QtCore.QRect(0, 0, 881, 571))
        self.myNotesTextInput.setObjectName("myNotesTextInput")
        self.myNotesScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.askLepTabWidget.addTab(self.myNotesTab, "")
        self.gridLayout.addWidget(self.askLepTabWidget, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)

        self.retranslateUi(askLepPage)
        self.askLepTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(askLepPage)

    def retranslateUi(self, askLepPage):
        _translate = QtCore.QCoreApplication.translate
        askLepPage.setWindowTitle(_translate("askLepPage", "Frame"))
        self.EnterExpressionLabel.setText(_translate("askLepPage", "Enter the Expression"))
        self.howToTextBox.setText(_translate("askLepPage", "Here\'s how to use the app: you just do it"))
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
        self.askLepTabWidget.setTabText(self.askLepTabWidget.indexOf(self.myNotesTab), _translate("askLepPage", "My Nptes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askLepPage = QtWidgets.QFrame()
    ui = Ui_askLepPage()
    ui.setupUi(askLepPage)
    askLepPage.show()
    sys.exit(app.exec_())
