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
        askLepWidgetFrame.resize(748, 866)
        self.verticalLayout = QtWidgets.QVBoxLayout(askLepWidgetFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.askLeProgramLabel = QtWidgets.QLabel(askLepWidgetFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.askLeProgramLabel.setFont(font)
        self.askLeProgramLabel.setObjectName("askLeProgramLabel")
        self.verticalLayout.addWidget(self.askLeProgramLabel)
        self.blackLine = QtWidgets.QFrame(askLepWidgetFrame)
        self.blackLine.setStyleSheet("background-color: rgb(24, 35, 32);")
        self.blackLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.blackLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.blackLine.setObjectName("blackLine")
        self.verticalLayout.addWidget(self.blackLine)
        self.logicalExpressionLabel = QtWidgets.QLabel(askLepWidgetFrame)
        self.logicalExpressionLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logicalExpressionLabel.setFont(font)
        self.logicalExpressionLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.logicalExpressionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logicalExpressionLabel.setObjectName("logicalExpressionLabel")
        self.verticalLayout.addWidget(self.logicalExpressionLabel)
        self.truthTableWidget = QtWidgets.QTableWidget(askLepWidgetFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.truthTableWidget.sizePolicy().hasHeightForWidth())
        self.truthTableWidget.setSizePolicy(sizePolicy)
        self.truthTableWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.truthTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.truthTableWidget.setStyleSheet("background-color: rgb(255, 255, 242);")
        self.truthTableWidget.setLineWidth(-3)
        self.truthTableWidget.setObjectName("truthTableWidget")
        self.truthTableWidget.setColumnCount(0)
        self.truthTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.truthTableWidget)
        self.dnfFormTitleLabel = QtWidgets.QLabel(askLepWidgetFrame)
        self.dnfFormTitleLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnfFormTitleLabel.setFont(font)
        self.dnfFormTitleLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.dnfFormTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dnfFormTitleLabel.setObjectName("dnfFormTitleLabel")
        self.verticalLayout.addWidget(self.dnfFormTitleLabel)
        self.satisfiabilityLabel = QtWidgets.QLabel(askLepWidgetFrame)
        self.satisfiabilityLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.satisfiabilityLabel.setFont(font)
        self.satisfiabilityLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.satisfiabilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.satisfiabilityLabel.setObjectName("satisfiabilityLabel")
        self.verticalLayout.addWidget(self.satisfiabilityLabel)
        self.validityLabel = QtWidgets.QLabel(askLepWidgetFrame)
        self.validityLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.validityLabel.setFont(font)
        self.validityLabel.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(255, 255, 242);")
        self.validityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.validityLabel.setObjectName("validityLabel")
        self.verticalLayout.addWidget(self.validityLabel)
        self.dnfExpressionLabel = QtWidgets.QLabel(askLepWidgetFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dnfExpressionLabel.setFont(font)
        self.dnfExpressionLabel.setStyleSheet("color: rgb(24, 35, 32);\n"
"background-color: rgb(255, 255, 242);")
        self.dnfExpressionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dnfExpressionLabel.setObjectName("dnfExpressionLabel")
        self.verticalLayout.addWidget(self.dnfExpressionLabel)

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
        self.dnfExpressionLabel.setText(_translate("askLepWidgetFrame", "DNF form (also the thing above is a table widget)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askLepWidgetFrame = QtWidgets.QWidget()
    ui = Ui_askLepWidgetFrame()
    ui.setupUi(askLepWidgetFrame)
    askLepWidgetFrame.show()
    sys.exit(app.exec_())
