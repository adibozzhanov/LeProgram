from os import path
import sqlite3

class Database:

    def __init__(self):
        self.dataBasePath = self.getLepDBFilePath()

    def getLepDBFilePath(self):
        basePath = path.dirname(__file__)
        return path.abspath(path.join(basePath, "..", "..", "data","database","lepDB.db"))

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
                               VALUES (?, ?, ?)""", (taskID, "", 0,))

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

    def updateAnswerExp(self, answerID, newAnswerExpression):
        
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Answers
                               SET (AnswerExp = ?)
                               WHERE AnswersID = ?""", (newAnswerExpression.getString(), answerID,))

        lepDB.commit()
        lepDB.close()

    def updateIsCorrect(self, answerID, isCorrectUpdate):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Answers
                               SET (isCorrect = ?)
                               WHERE AnswersID = ?""", (isCorrectUpdate, answerID,))

        lepDB.commit()
        lepDB.close()

    def deleteAnswer(self, answerID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""DELETE FROM Answers
                               WHERE AnswersID = ?  """, (answerID,))

        lepDB.commit()
        lepDB.close()

    def addNewTaskDB(self, testID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO Task(TestID, QuestionStatement, QuestionExpression)
                               VALUES(?, ?, ?)""", (testID, "", "",))

        lepDBCursor.execute("SELECT max(TaskID) FROM Task")
        lastTaskID = lepDBCursor.fetchone()[0]

        lepDB.commit()
        lepDB.close()

        return lastTaskID

    def loadTaskDB(self, taskID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT * FROM Task
                               WHERE TaskID = ?""", (taskID,))
        taskTuple = lepDBCursor.fetchone()

        lepDB.commit()
        lepDB.close()

        return taskTuple

    def updateTaskExpDB(self, taskID, newTaskExpression):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Task
                               SET (QuestionExpression = ?)
                               WHERE TaskID = ?""", (newTaskExpression, taskID,))

        lepDB.commit()
        lepDB.close()

    def updateTaskStatementDB(self, taskID, newTaskStatement):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Task
                               SET (QuestionStatement = ?)
                               WHERE TaskID = ?""", (newTaskStatement, taskID,))

        lepDB.commit()
        lepDB.close()

    def getAnswerIDfromTaskIDDB(self, taskID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT AnswersID FROM Answers
                               WHERE TaskID = ?""", (taskID,))

        listOfAnswerID = lepDBCursor.fetchall()

        lepDB.commit()
        lepDB.close()

        return listOfAnswerID

    def deleteTaskDB(self, taskID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""DELETE FROM Task
                               WHERE TaskID = ?  """, (taskID,))

        lepDB.commit()
        lepDB.close()

    def addNewTestDB(self):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO Test(TestName, TestDescription)
                               VALUES(?, ?)""", ("", "",))

        lepDBCursor.execute("SELECT max(TestID) FROM Test")
        lastTestID = lepDBCursor.fetchone()[0]

        lepDB.commit()
        lepDB.close()

        return lastTestID

    def loadTestDB(self, testID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT * FROM Test
                               WHERE TestID = ?""", (testID,))
        testTuple = lepDBCursor.fetchone()

        lepDB.commit()
        lepDB.close()
        return testTuple

    def updateTestNameDB(self, testID, newTestName):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Test
                               SET (TestName = ?)
                               WHERE TestID = ?""", (newTestName, testID,))

        lepDB.commit()
        lepDB.close()

    def updateTestDescriptionDB(self, testID, newDescription):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Test
                               SET (TestName = ?)
                               WHERE TestID = ?""", (newDescription, testID,))

        lepDB.commit()
        lepDB.close()

    def getTaskIDFromTestIDDB(self, testID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT TaskID FROM Task
                               WHERE TestID = ?""", (testID,))

        listOfTaskID = lepDBCursor.fetchall()

        lepDB.commit()
        lepDB.close()

        return listOfTaskID

    def addNewLibraryDB(self):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO Library(LibraryName)
                               VALUES(?)""", ("",))

        lepDBCursor.execute("SELECT max(LibraryID) FROM Library")
        lastLibraryID = lepDBCursor.fetchone()[0]

        lepDB.commit()
        lepDB.close()

        return lastLibraryID

    def loadLibraryDB(self, libraryID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT * FROM Library
                               WHERE LibraryID = ?""", (libraryID,))
        libraryTuple = lepDBCursor.fetchone()

        lepDB.commit()
        lepDB.close()

        return libraryTuple

    def updateLibraryNameDB(self, libraryID, newLibraryName):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Library
                               SET (LibraryName = ?)
                               WHERE LibraryID = ?""", (newLibraryName, libraryID,))

        lepDB.commit()
        lepDB.close()

    def lepDBAddTestIDandLibraryIDtoTesttoLibraryTableDB(self, testID, libraryID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO TestToLibrary(TestID, LibraryID)
                               VALUES(?,?)""", (testID,libraryID,))

        lepDB.commit()
        lepDB.close()

    def deleteTestToLibraryDB(self, testID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""DELETE FROM TestToLibrary
                               WHERE TestID = ?  """, (testID,))

        lepDB.commit()
        lepDB.close()

    def getTestIDFromLibraryIDDB(self, libraryID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT TestID FROM TestToLibrary
                               WHERE LibraryID = ?  """, (libraryID,))

        listOfTestID = lepDBCursor.fetchall()

        lepDB.commit()
        lepDB.close()

        return listOfTestID

    def addNewUser(self, libraryID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO Users(LibraryID, UserName)
                               VALUES(?,?)""", (libraryID, "",))

        lepDBCursor.execute("SELECT max(UserID) FROM Users")
        lastUserID = lepDBCursor.fetchone()[0]

        lepDB.commit()
        lepDB.close()

        return lastUserID

    def loadUsersDB(self, userID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""SELECT * FROM Users
                               WHERE UserID = ?""", (userID,))
        userTuple = lepDBCursor.fetchone()

        lepDB.commit()
        lepDB.close()

        return userTuple

    def updateUserName(self, userID, newUserName):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Users
                               SET (UserName = ?)
                               WHERE UserID = ?""", (newUserName, userID,))

        lepDB.commit()
        lepDB.close()


#a = Database()
#a.loadTestDB(1)
