from os import path


class Database:

    def __init__(self):
        self.dataBasePath = self.getLepDBFilePath()

    def getLepDBFilePath(self):
        basePath = path.dirname(__file__)
        return path.abspath(path.join(basePath, "..", "..", "data/databases/lepDB.db"))

    def addTestDB(self, testObj):
        # testObj will be created before
        # data can be accessed through getter methods 
        pass

    def getTestDB(self, testId):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("SELECT * FROM Test WHERE TestID = ?", (testId,))
        testData = databaseCursor.fetchone()

        databaseCursor.close()
        lepDB.commit()
        lepDB.close()

        return testData


    def getLibraryDB(self, libraryID): # <-- used to have a testID parameter changed to have LibraryID idk if it was a mistake
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT * FROM Library 
                               WHERE LibraryID = ?""", (libraryID,))
        libraryData = databaseCursor.fetchone()

        databaseCursor.close()
        lepDB.commit()
        lepDB.close()

        return libraryData


    def addNewAnswerDB(self, taskID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO answers (TaskID, AnswerExp, IsCorrect)
                               VALUES (?, ?, ?)""", (taskID, "", 0))

        # Getting the last ID
        lepDBCursor.execute("SELECT max(AnswersID) FROM Answers")
        lastAnswerID = lepDBCursor.fetchone[0]

        lepDB.commit()
        lepDB.close()

        return lastAnswerID

    def loadAnswerDB(self, answerID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT * FROM Answers 
                               WHERE AnswersID = ?""", (answerID,))
        answerTuple = lepDBCursor.fetchone()

        lepDB.commit()
        lepDB.close()
        return answerTuple

    def updateAnswerExp(self, answerID, newExpression):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Answers
                               SET (AnswerExp = ?)
                               WHERE AnswersID = ?""", (newExpression, answerID))

        lepDB.commit()
        lepDB.close()

    def updateIsCorrect(self, answerID, isCorrectUpdate):

        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Answers
                               SET (isCorrect = ?)
                               WHERE AnswersID = ?""", (isCorrectUpdate, answerID))

        lepDB.commit()
        lepDB.close()

    def addNewTaskdb(self):
        pass







a = Database()
#a.getLepDBFilePath()
