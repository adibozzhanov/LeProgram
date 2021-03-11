import sys
from lexparse import Node, getExpressionTree

NOT = "/NOT"
AND = "/AND"
OR = "/OR"
TOP = "/TOP"
BOT = "/BOT"

# in node
# def getExpressionString(self):
# def getTableRow(self, dict):
# def getVariables(self):

#/NOT (/NOT a /AND a /AND /BOT) /IMP a /XOR /NOT /NOT /TOP

#/NOT (/NOT b /AND a /AND /BOT) /IMP c /XOR /NOT /NOT /TOP


class logicEx(object): #can later add the function right to the node
    def __init__(self, exTree):
        self.exTree = exTree
        self.str = exTree.getExpressionString()
        self.variableValues = dict.fromkeys(exTree.getVariables(), None)
        self.truthTable = None
        self.tableFinalColumn = None
        self.satisfiable = None
        self.valid = None
        self.fdnf = None
        self.dnf = None
        self.fdnfStr = None
        self.dnfStr = None

    def getString(self):
        return self.str

    def getTruthTable(self):
        if not self.truthTable: self.generateAll()
        return self.truthTable

    def getDNF(self):
        if not self.fdnfStr: self.generateAll()
        return self.fdnfStr

    def getSimplified(self):
        if not self.dnfStr: self.generateAll()
        return self.dnfStr

    def getSatisfiable(self):
        if not self.satisfiable: self.generateAll()
        return self.satisfiable

    def getValid(self):
        if not self.valid: self.generateAll()
        return self.valid

    def generateAll(self):
        self.generateTable()
        self.generateFDNF()

    def generateTable(self): #edge case str len =1 v 0
        var = sorted(self.variableValues)
        table = []
        self.valid = True
        self.satisfiable = False

        table.append(var + [self.str])
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

    def generateFDNF(self):
        #if self.valid: print("DNF:",TOP)
        #elif not self.satisfiable : print("DNF:",BOT)
        if len(self.variableValues)==0:
            self.fdnf = self.exTree
            self.fdnfStr = self.str
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
                            cols.append(NOT + var[c])
                    rows.append(AND.join(cols))
            self.fdnf = getExpressionTree(OR.join(rows))
            self.fdnfStr = self.fdnf.getExpressionString()


    def printSimpleTable(self): #FOR TESTING
        t = self.getTruthTable()
        for r in t:
            for c in r:
                if len(c)==1:
                    print(c[0], end='\t')
                else:
                    print(c[self.tableFinalColumn], end= '\t')
            print()
        print("\nVALID:", self.valid)
        print("SATISFIABLE:", self.satisfiable)
        print("DNF with too many parenthesis:",self.fdnfStr)





        #for row in range(2**len(var)):
        #    for col in range(len(var)):
        #        b = row%(2**(len(var)-col)) == 0
        #        print(b)
