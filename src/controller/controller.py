import sys
from views.view import View
from models.model import Model
from models.expression import Expression
from models.lexerParser import getExpressionTree


DEFAULT_LIBRARY_ID = 1
DEFAULT_USER_ID = 1



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
            "randomQuestions": self.view.loadRandomQs,
            #"newTest" : self.view.loadNewTest,
            "testPreview": self.processTestPreview,
            #"loadAskLep": self.loadAskLep
        }


    def run(self):
        self.view.run()

    def processTestPreview(self):
        # get the test from the database
        # load the test view
        pass

    def loadMainPage(self, *args):
        # get main library

        # pass it to loadHome method
        self.view.loadHome(self.mainLibrary)

    def loadRandomTest(self, *args):
        complexity = args[0]
        # generateQuestion(complexity)
        # view.loadTask()

    def loadAskLep(self, *args):
        # takes [inputString]
        # return an expression instance
        inputString = args[0]
        view.updateAskLep(Expression(getExpressionTree(inputString)))





    def handleRequest(self, request, *args):
        # args - view can pass parameters to a controller
        # if args is empty it's equivalent to an empty function call
        print("Handling request: ", request)
        if request in self.requests:
            self.requests[request](*args)
        else:
            print(f"Error: request [{request}] not found, Loading not found screen")
            self.requests["notFound"]()
