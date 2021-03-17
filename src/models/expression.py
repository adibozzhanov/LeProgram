import sys
from parser import Node

NOT = "/NOT"
AND = "/AND"
OR = "/OR"
TOP = "/TOP"
BOT = "/BOT"


#/NOT (/NOT a /AND a /AND /BOT) /IMP a /XOR /NOT /NOT /TOP

#/NOT (/NOT b /AND a /AND /BOT) /IMP c /XOR /NOT /NOT /TOP


class Expression(object): #can later add the function right to the node
    def __init__(self, exTree):
        self.exTree = exTree
        self.str = exTree.getString()
        self.displayStr = exTree.getDisplayString()
        self.variableValues = dict.fromkeys(exTree.getVariables(), None)
        self.truthTable = None
        self.simpleTable = None
        self.tableFinalColumn = None
        self.satisfiable = None
        self.valid = None
        self.dnf = None

    def getString(self):
        return self.str

    def getDisplayString(self):
        return self.displayStr

    def getTruthTable(self):
        if not self.truthTable: self.__generateAll()
        return self.truthTable

    def getSimpleTable(self):
        if not self.simpleTable: self.__generateAll()
        return self.simpleTable

    def getTableFinalColumn(self):
        if not self.tableFinalColumn: self.__generateAll()
        return self.tableFinalColumn

    def getDNF(self):
        if not self.dnf: self.__generateAll()
        return self.dnf

    def getSatisfiable(self):
        if not self.satisfiable: self.__generateAll()
        return self.satisfiable

    def getValid(self):
        if not self.valid: self.__generateAll()
        return self.valid

    def __generateAll(self):
        self.__generateTable()
        self.__generateDNF()

    def __generateTable(self): #edge case str len =1 v 0
        var = sorted(self.variableValues)
        table = []
        self.valid = True
        self.satisfiable = False
        self.simpleTable = []

        table.append(var + [self.displayStr])
        cols = len(var)
        rows = 2**cols

        binStr = lambda x, n: format(x, 'b').zfill(n)
        for row in range(rows):
            tableRow = []
            bin = binStr(row,cols)
            for col in range(cols):
                b = (bin[col]=='0')
                tableRow.append([b])
                self.variableValues[var[col]] = b
            r = self.exTree.getTableRow(self.variableValues)

            self.simpleTable.append(r[0])
            if r[0]:
                self.satisfiable = True
            else:
                self.valid = False

            tableRow.append(r[1])
            table.append(tableRow)

            self.tableFinalColumn = r[2]

        #if (len(var)==1) and (len(self.str)==1):
        #    for r in table:
        #        r.pop()
        self.truthTable = table

    def __generateDNF(self):
        #if self.valid: print("DNF:",TOP)
        #elif not self.satisfiable : print("DNF:",BOT)
        if self.valid:
            self.dnf = "⊤"
        elif not self.satisfiable:
            self.dnf= "⊥"
        else:
            var = sorted(self.variableValues)
            rows=[]
            t = self.getTruthTable()[1:]
            for r in t:
                if r[-1][self.tableFinalColumn]:
                    cols = []
                    for c in range(len(r)-1):
                        if r[c][0]:
                            cols.append(var[c])
                        else:
                            cols.append("¬" + var[c])
                    rows.append("(" + " ∧ ".join(cols) + ")")
            self.dnf = (" ∨ ".join(rows))


    def printSimpleTable(self): #FOR TESTING
        t = self.getTruthTable()
        for r in t:
            for c in r:
                if len(c)==1:
                    print(c[0], end='\t')
                else:
                    print(c[self.tableFinalColumn], end= '\t')
            print()
        print("\nVALID:", self.getValid())
        print("SATISFIABLE:", self.getSatisfiable())
        print("DNF:",self.getDNF())





        #for row in range(2**len(var)):
        #    for col in range(len(var)):
        #        b = row%(2**(len(var)-col)) == 0
        #        print(b)
