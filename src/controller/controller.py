import sys
from views.view import View
from models.model import Model
from models.expression import Expression
from models.lexerParser import getExpressionTree
from models.randomTaskGenerator import TaskGenerator
from models.test import Test
from models.task import Task
from models.answer import Answer


class Controller:
    def __init__(self):
        self.model = Model()
        self.mainLibrary = self.model.getMainLibrary()
        self.view = View()
        self.loadMainPage(self.mainLibrary)
        self.view.registerRequestHandler(self.handleRequest)
        # request handlers in a dictionary
        # view will send requests to a controller
        # controller will do some magic and tell the view what to do
        # more in handleRequest() method
        self.requests = {
            "homePage" : self.loadMainPage,
            "notFound" : self.view.loadNotFound,
            "askLep": self.view.loadLep,
            #"user": self.view.loadUser,
            "startRandomTest": self.startRandomTest, 
            "randomQuestions": self.view.loadRandomQs,
            "newTest" : self.loadTestMaking,
            "testPreview": self.view.loadTestPreview,
            "loadAskLep": self.loadAskLep,
            "startTest": self.view.loadTestTaking,
            "saveTest": self.saveTest,
            "loadTestResultsPls": self.loadResultPage
        }


    def run(self):
        self.view.run()


    def startTest(self, test):
        self.view.loadTestTaking(test)

    def loadTestMaking(self):
        self.view.loadNewTest(self.mainLibrary)

    def startRandomTest(self, complexity, score = 0):
        generator = TaskGenerator(complexity)
        newTask = generator.getTask()
        self.view.startRandomTest(newTask, score, complexity)
        
        


    def loadMainPage(self, *args):
        # get main library
        # pass it to loadHome method
        self.view.loadHome(self.mainLibrary)


    def loadAskLep(self, *args):
        # takes [inputString]
        # adds an expression instance to askLep
        inputString = args[0]
        tree = getExpressionTree(inputString)

        if tree is not None:
            self.view.updateAskLep(Expression(tree))

    def saveTest(self, *args):
        # args - [TestName, Test Description, TaskArray]        #
        #     Task Array - [Task Statement, taskExpressoin ,(answers)]        #
        #     answer - [ answerExpression, Correctness: Boolean]
        test = Test()
        test.addThisTestToALibrary(self.mainLibrary.getLibraryId())
        test.setName(args[0])
        test.setDescription(args[1])
        argsTasks = args[2]
        for t in argsTasks:
            task = Task(test.getTestId())
            task.setStatement(t[0])
            task.setExpression(t[1])
            argsAnswers = t[2]
            for a in argsAnswers:
                answer = Answer(task.getTaskId())
                answer.setExpression(a[0])
                if a[1]: answer.setCorrect()
                task.addAnswer(answer)
            test.addTask(task)

    def loadResultPage(self, test):
        self.view.loadTestResult(test)
        

    def handleRequest(self, request, *args):
        # args - view can pass parameters to a controller
        # if args is empty it's equivalent to an empty function call
        if request in self.requests:
            self.requests[request](*args)
        else:
            self.requests["notFound"]()
