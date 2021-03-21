from models.library import Library
from models.lexerParser import Node, getExpressionTree
from models.expression import Expression
from models.database import Database

class User:
    def __init__(self, userId=None):
        if userId is None:
            self.name = None
            self.library = Library()
            # ADD A NEW LIB IN THE DATABASE
            self.id = 0 # GET THE NEW ID FROM THE DATABASE
        else:
            self.id = userId
            # LOAD DATA FROM THE DATABASE

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE

    def getName(self):
        return self.name

    def getLibrary(self):
        return self.library

    def getUserId(self):
        return self.id


if __name__ == '__main__': #testing
    if True:
        u = User()
        u.setName("Carmen")
        l = u.getLibrary()
        testId = l.addTestAndGetId()
        t = l.getTest(testId)
        t.setName("testytest")
        taskId = t.addTaskAndGetId()
        print(taskId)
        q = t.getTask(taskId)
        answerId = q.addAnswerAndGetId()
        t.addTaskAnswerGiven(taskId,answerId)
        print(t.tasksAnswered, t.correctAnswers)
        t.resetTest()
        print(t.tasksAnswered, t.correctAnswers)
        taskId = t.addTaskAndGetId()
        print(taskId)
        q = t.getTask(taskId)
        answerId = q.addAnswerAndGetId()
        a = q.getAnswer(answerId)
        a.setCorrect()
        t.addTaskAnswerGiven(taskId,answerId)
        print(t.tasksAnswered, t.correctAnswers)
        print(t.getScore())
        while True:
            try:
                text = input('>')
            except EOFError:
                break
            if text:
                print("-"*20, "TREE:")
                tree = getExpressionTree(text)
                ex = Expression(tree)
                print("-"*20, "THE EXPRESSION:")
                print("ex: ",ex.getString())
                print("ex: ",ex.getDisplayString())
                print("-"*20, "SIMPLIFIED TABLE:")
                ex.printSimpleTable()

#/NOT (/NOT b /AND a /AND /BOT) /IMP c /XOR /NOT /NOT /TOP
