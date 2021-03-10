
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
        self.formula = formula #input is dict and output bool
        self.symbol = symbol #string:)

    def add_child(self, obj):
        self.children.append(obj)

    def evaluate(self, dict):
        if len(self.children)==2:
            return self.formula(self.children[0].evaluate(dict),self.children[1].evaluate(dict))
        elif len(self.children)==1:
            return self.formula(self.children[0].evaluate(dict))
        elif len(self.children)==0:
            return self.formula(self.data, dict)

        else:
            print("ERROR:) too many kids hun")

    #def evaluate(self, dict):
        #return self.


#/NOT (/NOT a /OR a /AND /BOT) /IMP a /OR /NOT /NOT /TOP
# → ↔ ¬ ∧ ∨ ⊤ ⊥
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
    debugfile = 'parser.out'
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
        return Node(p.NAME, p.NAME, lambda name, dict: dict[name])

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
        n.add_child(p.ex)
        return n

    @_('ex AND ex')
    def ex(self, p):
        n = Node(p.AND, "∧", lambda b1, b2: b1 and b2)
        n.add_child(p.ex0)
        n.add_child(p.ex1)
        return n

    @_('ex OR ex')
    def ex(self, p):
        n = Node(p.OR, "∨", lambda b1, b2: b1 or b2)
        n.add_child(p.ex0)
        n.add_child(p.ex1)
        return n

    @_('ex XOR ex')
    def ex(self, p):
        n = Node(p.XOR, "⊕", lambda b1, b2: b1 != b2)
        n.add_child(p.ex0)
        n.add_child(p.ex1)
        return n

    @_('ex IFF ex')
    def ex(self, p):
        n = Node(p.IFF, "↔", lambda b1, b2: b1 == b2)
        n.add_child(p.ex0)
        n.add_child(p.ex1)
        return n

    @_('ex IMP ex')
    def ex(self, p):
        n = Node(p.IMP, "→", lambda b1, b2: (not b1) or b2)
        n.add_child(p.ex0)
        n.add_child(p.ex1)
        return n





if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    while True:
        try:
            text = input('>')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            pprint_tree(tree)

            print(tree.evaluate({'a':True}))
