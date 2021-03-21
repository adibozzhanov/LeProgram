from models.test import Test
from models.database import Database

class Library:
    def __init__(self, libraryId=None):

        self.lepDB = Database()

        if libraryId is None:
            self.name = None
            self.tests = {}
            self.user = None
            # ADD A NEW LIB IN THE DATABASE
            self.id = self.lepDB.addNewLibraryDB() # GET THE NEW ID FROM THE DATABASE
        else:
            self.id = libraryId
            self.tests = None
            # LOAD DATA FROM THE DATABASE
            libraryInfoTuple = self.lepDB.loadLibraryDB(self.id)
            self.name = libraryInfoTuple[1]

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE
        self.lepDB.updateLibraryNameDB(self.id, newName)

    def addTestAndGetId(self):
        t = Test()
        self.tests[t.getTestId()] = t
        # UPDATE THE DATABASE update the joining table
        self.lepDBAddTestIDandLibraryIDtoTesttoLibraryTableDB(t.getTestId(), self.id)
        return t.getTestId()

    def removeTest(self, testId):
        del self.tests[testId]
        # UPDATE THE DATABASE
        self.deleteTestToLibraryDB(testId)

    def getLibraryId(self):
        return self.id

    def getName(self):
        return self.name

    def getTest(self, testId):
        if self.tests is None:
            ids=[testId] #GET ALL THE TEST IDS FROME THE DATABASE
            for i in ids:
                self.__loadTest(i)
        return self.tests[testId]

    def getTests(self):
        if self.tests is None:
            ids=self.lepDB.getTestIDFromLibraryIDDB(self.id) #GET ALL THE TEST IDS FROME THE DATABASE
            for i in ids:
                self.__loadTest(i[0])
        return self.tests

    def __loadTest(self, testId):
        t = Test(testId=testId)
        self.tests[t.getTestId()] = t
