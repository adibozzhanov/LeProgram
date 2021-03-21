from lexerParser import getExpressionTree
from library import Library
from user import User
from RandomTaskGenerator import TaskGenerator
from test import Test
from answer import Answer
from task import Task
from expression import Expression

class Model():
    #getter methods
    def getMainLibrary(self):
        return Library()

    def getUser(self):
        return User()

    def getRandomTaskGenerator(self, complexity):
        return TaskGenerator(complexity)

    def getExpression(self, inputString):
        # take a string in and return expression object
        # returns None if fails
        return Expression(getExpressionTree(inputString))

    #adder methods
    def addNewTest(self): # again why do we need this here the library has this mehtod,
        return Test()

    def addNewTask(slef, testId): #??
        return Task(testId)

    def addNewAnswer(self, taskId): # waaaaait adi why do we need this? the task has those methods
        return Answer(taskId)
