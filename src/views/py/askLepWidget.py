from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

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

            self.truthTableWidget.setRowCount(len(expResults) + 1)
            self.truthTableWidget.setColumnCount(len(columnInfo) + len(expressionSplit) - 1)

            # Setting the headings
            for columnVarInd in range(len(columnInfo)):
                self.truthTableWidget.setItem(0, columnVarInd, QTableWidgetItem(columnInfo[columnVarInd]))

            for columnExpInd in range(len(expressionSplit)):
                self.truthTableWidget.setItem(0, columnVarInd + columnExpInd, QTableWidgetItem(expressionSplit[columnExpInd]))

            # Populate the table
            for expResultsInd in range(len(expResults)):

                # Filling in the variable inputs

                if len(columnInfo) == 1:
                    for expVarInpInd in range(len(columnInfo)):
                        if truthTable[expResultsInd + 1][expVarInpInd][0] == True:
                            stringRes = "T"
                        else:
                            stringRes = "F"

                        self.truthTableWidget.setItem(expResultsInd + 1, expVarInpInd, QTableWidgetItem(stringRes))

                else:
                    for expVarInpInd in range(len(columnInfo) - 1):

                        if truthTable[expResultsInd + 1][expVarInpInd][0] == True:
                            stringRes = "T"
                        else:
                            stringRes = "F"

                        self.truthTableWidget.setItem(expResultsInd + 1, expVarInpInd, QTableWidgetItem(stringRes))

                # Filling in the expression outputs
                outRes = truthTable[expResultsInd + 1][-1]

                for outResInd in range(len(outRes)):

                    if outRes[outResInd] == True:
                        outResString = "T"
                    elif outRes[outResInd] == False:
                        outResString = "F"
                    else:
                        outResString = ""
                    self.truthTableWidget.setItem(expResultsInd + 1, expVarInpInd + outResInd + 1, QTableWidgetItem(outResString))

        # Resize the cells to make table look better
        self.truthTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Hiding the column and row headers
        self.truthTableWidget.verticalHeader().setVisible(False)
        self.truthTableWidget.horizontalHeader().setVisible(False)

        # Removed the empty columns
        for remIndex in range(self.truthTableWidget.columnCount(), 0, -1):
            if self.truthTableWidget.item(0, remIndex - 1).text() == " ":
                self.truthTableWidget.removeColumn(remIndex - 1)


