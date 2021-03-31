# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/askLePWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_askLepWidgetFrame(object):
    def setupUi(self, askLepWidgetFrame):
        askLepWidgetFrame.setObjectName("askLepWidgetFrame")
        askLepWidgetFrame.resize(750, 628)
        askLepWidgetFrame.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(askLepWidgetFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(askLepWidgetFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.askLeProgramLabel = QtWidgets.QLabel(self.frame)
        self.askLeProgramLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.askLeProgramLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.askLeProgramLabel.setFont(font)
        self.askLeProgramLabel.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"")
        self.askLeProgramLabel.setObjectName("askLeProgramLabel")
        self.verticalLayout_2.addWidget(self.askLeProgramLabel)
        self.blackLine = QtWidgets.QFrame(self.frame)
        self.blackLine.setStyleSheet("background-color: rgb(24, 35, 32);")
        self.blackLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.blackLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.blackLine.setObjectName("blackLine")
        self.verticalLayout_2.addWidget(self.blackLine)
        self.logicalExpressionLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logicalExpressionLabel.sizePolicy().hasHeightForWidth())
        self.logicalExpressionLabel.setSizePolicy(sizePolicy)
        self.logicalExpressionLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.logicalExpressionLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logicalExpressionLabel.setFont(font)
        self.logicalExpressionLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.logicalExpressionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logicalExpressionLabel.setObjectName("logicalExpressionLabel")
        self.verticalLayout_2.addWidget(self.logicalExpressionLabel)
        self.truthTableWidget = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.truthTableWidget.sizePolicy().hasHeightForWidth())
        self.truthTableWidget.setSizePolicy(sizePolicy)
        self.truthTableWidget.setMinimumSize(QtCore.QSize(300, 400))
        self.truthTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.truthTableWidget.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"")
        self.truthTableWidget.setLineWidth(-3)
        self.truthTableWidget.setObjectName("truthTableWidget")
        self.truthTableWidget.setColumnCount(0)
        self.truthTableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.truthTableWidget)
        self.dnfFormTitleLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dnfFormTitleLabel.sizePolicy().hasHeightForWidth())
        self.dnfFormTitleLabel.setSizePolicy(sizePolicy)
        self.dnfFormTitleLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.dnfFormTitleLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnfFormTitleLabel.setFont(font)
        self.dnfFormTitleLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.dnfFormTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dnfFormTitleLabel.setWordWrap(True)
        self.dnfFormTitleLabel.setObjectName("dnfFormTitleLabel")
        self.verticalLayout_2.addWidget(self.dnfFormTitleLabel)
        self.satisfiabilityLabel = QtWidgets.QLabel(self.frame)
        self.satisfiabilityLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.satisfiabilityLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.satisfiabilityLabel.setFont(font)
        self.satisfiabilityLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.satisfiabilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.satisfiabilityLabel.setObjectName("satisfiabilityLabel")
        self.verticalLayout_2.addWidget(self.satisfiabilityLabel)
        self.validityLabel = QtWidgets.QLabel(self.frame)
        self.validityLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.validityLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.validityLabel.setFont(font)
        self.validityLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.validityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.validityLabel.setObjectName("validityLabel")
        self.verticalLayout_2.addWidget(self.validityLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(askLepWidgetFrame)
        QtCore.QMetaObject.connectSlotsByName(askLepWidgetFrame)

    def retranslateUi(self, askLepWidgetFrame):
        _translate = QtCore.QCoreApplication.translate
        askLepWidgetFrame.setWindowTitle(_translate("askLepWidgetFrame", "Form"))
        self.askLeProgramLabel.setText(_translate("askLepWidgetFrame", "Ask Le Program"))
        self.logicalExpressionLabel.setText(_translate("askLepWidgetFrame", "( ¬P ∨ ¬Q ) → ¬(Q ∧ R)"))
        self.truthTableWidget.setWhatsThis(_translate("askLepWidgetFrame", "Truth Table"))
        self.dnfFormTitleLabel.setText(_translate("askLepWidgetFrame", "DNF form:"))
        self.satisfiabilityLabel.setText(_translate("askLepWidgetFrame", "Satisfiability:"))
        self.validityLabel.setText(_translate("askLepWidgetFrame", "Validity:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askLepWidgetFrame = QtWidgets.QWidget()
    ui = Ui_askLepWidgetFrame()
    ui.setupUi(askLepWidgetFrame)
    askLepWidgetFrame.show()
    sys.exit(app.exec_())
