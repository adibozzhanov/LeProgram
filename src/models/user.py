from models.library import Library
from models.lexerParser import Node, getExpressionTree
from models.expression import Expression
from models.database import Database

class User:
    def __init__(self, userId=None):

        self.lepDB = Database()

        if userId is None:
            self.name = None
            self.library = Library() # <-- adds a new lib to the db
            # ADD A NEW A NEW USER IN THE DATABASE
            self.id = self.lepDB.addNewUser(self.library.getLibraryID()) # GET THE NEW ID FROM THE DATABASE
        else:
            self.id = userId
            # LOAD DATA FROM THE DATABASE
            userInfoTuple = self.lepDB.loadUsersDB(self.id)

            self.library = Library(userInfoTuple[1])
            self.name = userInfoTuple[2]

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE
        self.lepDB.updateUserName(self.id, newName)

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
