class User:
    counter = 0
    def __init__(self, userId=None):
        if userId is None:
            self.id = type(self).counter
            type(self).counter+=1
            self.name = None
            self.library = Library()
            # ADD A NEW LIB IN THE DATABASE
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
