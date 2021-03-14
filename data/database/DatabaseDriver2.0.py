import sqlite3, os

def createLepDB():

    # Only creates the database if it doesn't exist
    if not os.path.isfile("lepDB.db"):
        # Creating the database
        lepDB = sqlite3.connect("lepDB.db")
        lepDB.commit()
        lepDB.close()

def createUserTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    Users(UserID INTEGER PRIMARY KEY AUTOINCREMENT, LibraryID INTEGER, UserName TEXT, FOREIGN KEY(LibraryID) REFERENCES Library(LibraryID))""")
    lepDB.cursor().close()
    lepDB.commit()
    lepDB.close()

def createLibraryTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    Library (LibraryID INTEGER PRIMARY KEY AUTOINCREMENT, LibraryName TEXT)""")
    lepDB.cursor().close()
    lepDB.commit()
    lepDB.close()

def createTestToLibraryTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS 
    TestToLibrary (TestID INTEGER, LibraryID INTEGER, FOREIGN KEY(TestID) REFERENCES Test(TestID), FOREIGN KEY (LibraryID) REFERENCES Library (LibraryID))""")
    lepDB.cursor().close()
    lepDB.commit()
    lepDB.close()

def createTestTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    Test (TestID INTEGER PRIMARY KEY AUTOINCREMENT, TestName TEXT, TestDescription TEXT)""")
    lepDB.cursor().close()
    lepDB.commit()
    lepDB.close()

def createTaskTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    Task (TaskID INTEGER PRIMARY KEY AUTOINCREMENT, TestID INTEGER, QuestionStatement TEXT, QuestionExpression TEXT, FOREIGN KEY(TestID) REFERENCES Test(TestID))""")
    lepDB.commit()
    lepDB.close()

def createAnswersTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    Answers (AnswersID INTEGER PRIMARY KEY AUTOINCREMENT, TaskID INTEGER, AnswerExp TEXT, IsCorrect INTEGER, FOREIGN KEY(TaskID) REFERENCES Task(TaskID))""")
    lepDB.cursor().close()
    lepDB.commit()
    lepDB.close()

def createTagsToTestTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    TagsToTest (TagID INTEGER, TestID INTEGER, FOREIGN KEY(TagID) REFERENCES Tags(TagID), FOREIGN KEY(TestID) REFERENCES Test(TestID))""")
    lepDB.cursor().close()
    lepDB.commit()
    lepDB.close()

def createTagsTable():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute(""" CREATE TABLE IF NOT EXISTS
    Tags (TagID INTEGER PRIMARY KEY AUTOINCREMENT, TagName TEXT)""")
    lepDB.commit()
    lepDB.close()

# Just in case foreign keys gets turned off somehow
def turnFKOn():
    lepDB = sqlite3.connect("lepDB.db")
    lepDB.cursor().execute("pragma foreign_keys=on")
    lepDB.commit()
    lepDB.close()

def createAllTables():
    #turnFKOn()
    createLepDB()
    createLibraryTable()
    createTestTable()
    createTagsTable()
    createTestToLibraryTable()
    createTagsToTestTable()
    createUserTable()
    createTaskTable()
    createAnswersTable()

createAllTables()
