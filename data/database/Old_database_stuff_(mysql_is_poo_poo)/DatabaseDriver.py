import mysql.connector

lepDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database = "lepDatabase"
)

def createUserTable():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE TABLE Users (UserID int PRIMARY KEY AUTO_INCREMENT, LibraryID int, FOREIGN  KEY(LibraryID) REFERENCES Library(LibraryID), UserName VARCHAR(50))")
    lepCursor.close()

def createLibaryTable():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE TABLE Library (LibraryID int PRIMARY KEY AUTO_INCREMENT, LibraryName VARCHAR(50))")
    lepCursor.close()

def createTestToLibraryTable():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE TABLE TestToLibrary (TestID int, FOREIGN KEY(TestID) REFERENCES Test(TestID), LibraryID int, FOREIGN KEY(LibraryID) REFERENCES Library(LibraryID))")
    lepCursor.close()

def createTestTable():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE TABLE Test (TestID int PRIMARY KEY AUTO_INCREMENT, TestName VARCHAR(50), TestDescription VARCHAR(500))")
    lepCursor.close()

def createTaskTable():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE TABLE Task (TaskID int PRIMARY KEY AUTO_INCREMENT, TestID int, FOREIGN KEY(TestID) REFERENCES Test(TestID), QuestionStatement VARCHAR(500), QuestionExpression VARCHAR(500))")
    lepCursor.close()


def createAnswersTable():
  lepCursor = lepDB.cursor()
  lepCursor.execute("CREATE TABLE Answers (AnswersID int PRIMARY KEY AUTO_INCREMENT, TaskID int, FOREIGN KEY(TaskID) REFERENCES Task(TaskID), Expression VARCHAR(500), IsCorrect int)")
  lepCursor.close()

def createTagsToTestTable():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE TABLE TagsToTest (TagID int, FOREIGN KEY(TagID) REFERENCES Tags(TagID), TestID int, FOREIGN KEY(TestID) REFERENCES Test(TestID))")
    lepCursor.close()

def createTagsTable():
    lepCusor = lepDB.cursor()
    lepCusor.execute("CREATE TABLE Tags (TagID int PRIMARY KEY AUTO_INCREMENT, TagName VARCHAR(50))")
    lepCusor.close()

def createAllTables():
    createLibaryTable()
    createTestTable()
    createTagsTable()
    createTestToLibraryTable()
    createTagsToTestTable()
    createUserTable()
    createTaskTable()
    createAnswersTable()

createAllTables()


