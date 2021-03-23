from PyQt5 import QtCore, QtGui, QtWidgets

from views.py.askLepWidgetQt import Ui_askLepWidgetFrame


class AskLepWidget(Ui_askLepWidgetFrame):

    def __init__(self, master, view, expression):
        self.view = view
        self.expression = expression
        self.setupUi(master)
        self.setExpressionInfo(self.expression)

    def setExpressionInfo(self, expression):
        if expression is not None:
            # Set Expression
            self.logicalExpressionLabel.setText(expression.getDisplayString())
            self.logicalExpressionLabel.adjustSize()

            # Set DNF
            self.dnfFormTitleLabel.setText(expression.getDNF())
            self.dnfFormTitleLabel.adjustSize()

            # Set Satisfiability
            self.satisfiabilityLabel.setText(str(expression.getSatisfiable()))
            self.satisfiabilityLabel.adjustSize()

            # Set Validity
            self.validityLabel.setText((expression.getValid()))
            self.validityLabel.adjustSize()
