import sys
from lexparse import Node, getExpressionTree
from logicEx import logicEx


if __name__ == '__main__':
    while True:
        try:
            text = input('>')
        except EOFError:
            break
        if text:
            print("-"*20, "TREE:")
            tree = getExpressionTree(text)
            ex = logicEx(tree)
            print("-"*20, "THE EXPRESSION:")
            print("ex: ",ex.getString())
            print("-"*20, "SIMPLIFIED TABLE:")
            ex.printSimpleTable()
            """try:
                tree = getExpressionTree(text)
                ex = logicEx(tree)
                print("ex: ",ex.getString())
                ex.generateTable()
            except: print("whooopsie")"""
