from models.lexerParser import getExpressionTree
from models.library import Library
from models.user import User
from models.randomTaskGenerator import TaskGenerator
from models.test import Test
from models.answer import Answer
from models.task import Task
from models.expression import Expression

class Model():
    #getter methods
    def getMainLibrary(self, libraryId=1):
        return Library(libraryId)

    def getUser(self, userId):
        return User(userId)

    def getRandomTaskGenerator(self, complexity):
        return TaskGenerator(complexity)

    def getExpression(self, inputString):
        # take a string in and return expression object
        # returns None if fails
        return Expression(getExpressionTree(inputString))

    # adder methods
    # def addNewTest(self): # again why do we need this here the library has this mehtod,
    #     return Test()
    #
    # def addNewTask(slef, testId):
    #     return Task(testId)
    #
    # def addNewAnswer(self, taskId): # waaaaait adi why do we need this? the task has those methods
    #     return Answer(taskId)
