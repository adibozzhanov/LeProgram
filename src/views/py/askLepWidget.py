from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

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
            self.dnfFormTitleLabel.setText(f"DNF: {expression.getDNF()}")
            self.dnfFormTitleLabel.adjustSize()

            # Set Satisfiability
            self.satisfiabilityLabel.setText(f"Satisfiable: {expression.getSatisfiable()}")
            self.satisfiabilityLabel.adjustSize()

            # Set Validity
            self.validityLabel.setText(f"Valid: {expression.getValid()}")
            self.validityLabel.adjustSize()

            truthTable = expression.getTruthTable()
            expResults = expression.getSimpleTable()

            columnInfo = truthTable[0]
            expressionSplit = list(columnInfo[-1])
            print(expressionSplit)

            self.truthTableWidget.setRowCount(len(expResults) + 1)
            self.truthTableWidget.setColumnCount(len(columnInfo) + len(expressionSplit) - 1)

            # Setting the headings
            for columnVarInd in range(len(columnInfo)):
                self.truthTableWidget.setItem(0, columnVarInd, QTableWidgetItem(columnInfo[columnVarInd]))

            for columnExpInd in range(len(expressionSplit)):
                self.truthTableWidget.setItem(0, columnVarInd + columnExpInd, QTableWidgetItem(expressionSplit[columnExpInd]))

            # Populate the table
            for expResultsInd in range(len(expResults)):

                for expVarInpInd in range(len(columnInfo) - 1):

                    if truthTable[expResultsInd + 1][expVarInpInd][0] == True:
                        stringRes = "True"
                    else:
                        stringRes = "False"

                    self.truthTableWidget.setItem(expResultsInd + 1, expVarInpInd, QTableWidgetItem(stringRes))

                outRes = truthTable[expResultsInd + 1][2]

                for outResInd in range(len(outRes)):
                    if outRes[outResInd] == True:
                        outResString = "True"
                    elif outRes[outResInd] == False:
                        outResString = "False"
                    else:
                        outResString = ""

                    self.truthTableWidget.setItem(expResultsInd + 1, expVarInpInd + outResInd + 1, QTableWidgetItem(outResString))
                    #print(type(truthTable[expResultsInd + 1][expVarInpInd][0]))
            #print(truthTable)

            #print(truthTable)
