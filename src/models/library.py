from test import Test

class Library:
    counter = 0
    def __init__(self, libraryId=None):
        if libraryId is None:
            self.id = type(self).counter
            type(self).counter+=1
            self.name = None
            self.tests = {}
            self.user = None
            # ADD A NEW LIB IN THE DATABASE
        else:
            self.id = libraryId
            self.tests = None
            # LOAD DATA FROM THE DATABASE

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE

    def addTestAndGetId(self):
        t = Test()
        self.tasks[t.getTestId()] = t
        # UPDATE THE DATABASE
        return t.getTestId()

    def removeTest(self, testId):
        del self.tests[testId]
        # UPDATE THE DATABASE

    def getLibraryId(self):
        return self.id

    def getName(self):
        return self.name

    def getTest(self, testId):
        if self.tests is None:
            ids=[] #GET ALL THE ANSWER IDS FROME THE DATABASE
            for i in ids:
                self.__loadTest(i)
        return self.tests[testId]

    def getTests(self):
        if self.tests is None:
            ids=[] #GET ALL THE ANSWER IDS FROME THE DATABASE
            for i in ids:
                self.__loadTest(i)
        return self.tests

    def __loadTest(self, testId):
        t = Test(testId=testId)
        self.tests[t.getTestId()] = t
