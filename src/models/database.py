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
                               WHERE AnswersID = ?""", (newAnswerExpression, answerID,))

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

        lepDBCursor.execute("""SELECT answerID FROM Answers
                               WHERE TaskID = ?""", (taskID,))

        listOfAnswerID = lepDB.fetchall()

        lepDB.commit()
        lepDB.close()

        return listOfAnswerID

    def deleteTaskDB(self, taskID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""DELETE FROM Task
                               WHERE TaskID = ?  """, (TaskID,))

        lepDB.commit()
        lepDB.close()

    def addNewTestDB(self):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO Test(TestName, TestDescription)
                               VALUES(?, ?)""", ("", "",))

        lepDBCursor.execute("SELECT max(TestID) FROM Test")
        lastTestID = lepDBCursor.fetchone[0]

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

    def updateTestNameDB(self, testID, newName):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""UPDATE Test
                               SET (TestName = ?)
                               WHERE TestID = ?""", (newName, testID,))

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

        listOfAnswerID = lepDB.fetchall()

        lepDB.commit()
        lepDB.close()


#a = Database()
#a.loadTestDB(1)
