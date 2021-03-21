import sys
from views.view import View
from models.model import Model

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
        
        
        

    def handleRequest(self, request, *args):
        # args - view can pass parameters to a controller
        # if args is empty it's equivalent to an empty function call
        print("Handling request: ", request)
        if request in self.requests:
            self.requests[request](*args)
        else:
            print(f"Error: request [{request}] not found, Loading not found screen")
            self.requests["notFound"]()
        



    def nameIsValid(self, name):
        # name: string
        # returns: boolean

        pass

    
    def validateExpression(self, expr):
        # expr: string of the expression
        # returns:   incorrect -> False
        #              correct -> [AST]

        pass

    def createLibrary(self, fields):
        # checks if the name of the library is valid and then
        
        pass

    def createTask(self, fields):
        # 
        pass


    # controller - Model communication

    def getLibrary(self):

        pass


    def getTask(self,id):

        pass
        
