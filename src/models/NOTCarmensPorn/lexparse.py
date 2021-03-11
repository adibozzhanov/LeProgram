
from sly import Lexer, Parser

def pprint_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", node.data, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)

class Node(object): #can later add the function right to the node
    def __init__(self, data, symbol, formula):
        self.data = data
        self.children = []
        self.variables = set()
        self.formula = formula #input is dict and output bool
        self.symbol = symbol #string:)
        self.str = None

    def addChild(self, obj):
        self.children.append(obj)

    def getVariables(self):
        return self.variables.copy()

    def getExpressionString(self):
        if not self.str: self.str = self.createString()
        return self.str

    def getTableRow(self, dict): #returns all values (I guess this type of stuff could be useful for logic gates)
        # [total value, [all values for the table], index of last value]
        if len(self.children)==2:
            left = self.children[0].getTableRow(dict)
            right = self.children[1].getTableRow(dict)
            current = self.formula(left[0],right[0])
            return [current, [None] + left[1] + [None,current,None] + right[1] + [None], len(left[1])+2]
        elif len(self.children)==1:
            right = self.children[0].getTableRow(dict)
            current = self.formula(right[0])
            return [current, [current] + right[1], 0]
        elif len(self.children)==0:
            return [self.formula(self.data, dict),[None],0]
        else:
            print("ERROR:) too many kids hun")


    def evaluate(self, dict): #this only returns the final value ATM USELESS
        if len(self.children)==2:
            return self.formula(self.children[0].evaluate(dict),self.children[1].evaluate(dict))
        elif len(self.children)==1:
            return self.formula(self.children[0].evaluate(dict))
        elif len(self.children)==0:
            return self.formula(self.data, dict)
        else:
            print("ERROR:) too many kids hun")

    def createString(self):
        if len(self.children)==2:
            return ("(" + self.children[0].createString() + " " +self.symbol + " " + self.children[1].createString() + ")")
        elif len(self.children)==1:
            return ( self.symbol + self.children[0].createString() )
        elif len(self.children)==0:
            return (self.symbol)
        else:
            print("ERROR:) too many kids hun")

    def updateVariables(self):
        for child in self.children:
            self.variables.update(child.variables)


#/NOT (/NOT a /OR a /AND /BOT) /IMP a /OR /NOT /NOT /TOP
# → ↔ ¬ ∧ ∨ ⊤ ⊥ (¬((¬a∧a)∧⊥)→(a⊕¬¬⊤)) (¬((¬a ∧ a) ∧ ⊥) → (a ⊕ ¬¬⊤))

#/NOT (/NOT a /AND a /AND /BOT) /IMP a /XOR /NOT /NOT /TOP


class BasicLexer(Lexer):
    tokens = { NAME, NOT, AND, OR, XOR, IMP, IFF, TOP, BOT }
    ignore = ' \t'

    literals = {'(', ')'}

    # Define tokens
    NAME = r'[a-zA-Z]'
    NOT = r'/NOT'
    AND = r'/AND'
    OR  = r'/OR'
    XOR = r'/XOR'
    IMP = r'/IMP'
    IFF = r'/IFF'
    TOP = r'/TOP'
    BOT = r'/BOT'


class BasicParser(Parser):
    #debugfile = 'parser.out'
    tokens = BasicLexer.tokens

    precedence = (
        ('left', IFF),
        ('left', IMP),
        ('left',  OR, XOR),
        ('left', AND),
        ('right', NOT),
        )

    @_('NAME')
    def ex(self, p):
        n = Node(p.NAME, p.NAME, lambda name, dict: dict[name])
        n.variables.add(p.NAME)
        return n

    @_('TOP')
    def ex(self, p):
        return Node(p.TOP, "⊤", lambda name, dict: True)

    @_('BOT')
    def ex(self, p):
        return Node(p.BOT, "⊥", lambda name, dict: False)

    @_('"(" ex ")"')
    def ex(self, p):
        return p.ex

    @_('NOT ex')
    def ex(self, p):
        n = Node(p.NOT, "¬", lambda b: not b)
        n.addChild(p.ex)
        n.updateVariables()
        return n

    @_('ex AND ex')
    def ex(self, p):
        n = Node(p.AND, "∧", lambda b1, b2: b1 and b2)
        n.addChild(p.ex0)
        n.addChild(p.ex1)
        n.updateVariables()
        return n

    @_('ex OR ex')
    def ex(self, p):
        n = Node(p.OR, "∨", lambda b1, b2: b1 or b2)
        n.addChild(p.ex0)
        n.addChild(p.ex1)
        n.updateVariables()
        return n

    @_('ex XOR ex')
    def ex(self, p):
        n = Node(p.XOR, "⊕", lambda b1, b2: b1 != b2)
        n.addChild(p.ex0)
        n.addChild(p.ex1)
        n.updateVariables()
        return n

    @_('ex IFF ex')
    def ex(self, p):
        n = Node(p.IFF, "↔", lambda b1, b2: b1 == b2)
        n.addChild(p.ex0)
        n.addChild(p.ex1)
        n.updateVariables()
        return n

    @_('ex IMP ex')
    def ex(self, p):
        n = Node(p.IMP, "→", lambda b1, b2: (not b1) or b2)
        n.addChild(p.ex0)
        n.addChild(p.ex1)
        n.updateVariables()
        return n

def getExpressionTree(inputString):
    lexer = BasicLexer()
    parser = BasicParser()
    try:
        tree = parser.parse(lexer.tokenize(inputString))
        pprint_tree(tree)
    except:
        print("Parsing failed, btw how we doing errors:)")
        tree = None
    return(tree)

'''
if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    while True:
        try:
            text = input('>')
        except EOFError:
            break
        if text:
            try:
                tree = parser.parse(lexer.tokenize(text))
                pprint_tree(tree)
                print(tree)
            except: print("whooopsie")'''

            #print(tree.getTableRow({'a':True}))
            #print(tree.getExpressionString())
