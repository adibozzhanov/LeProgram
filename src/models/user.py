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
            self.id = self.lepDB.addNewUser(self.library.getLibraryId()) # GET THE NEW ID FROM THE DATABASE
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
