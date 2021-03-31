from models.task import Task
from models.database import Database

class Test:
    # can either be initialized by the testId if it is already in the database
    # or by creating a new task if no id is given
    def __init__(self, testId=None):
        # OSCAR NO CLUE HOW OR WHERE BUT YOU NEED TO CREATE THE LIBRARY TO TESTS TABLE AND ACTUALLY STICK THE DATA THERE SOMEHOW

        self.lepDB = Database()

        if testId is None:
            self.name = None
            self.description = ""
            self.tasks = {}
            self.tags = {} #we need a tag class? or what do we do with them
            # ADD A NEW TEST IN THE DATABASE
            self.id = self.lepDB.addNewTestDB()

            #self.id = 0 # GET THE NEW ID FROM THE DATABASE
        else:
            self.id = testId
            self.tasks = None # only create the task instances when they ate requested
            # LOAD DATA FROM THE DATABASE
            testInfoTuple = self.lepDB.loadTestDB(self.id)
            self.name = testInfoTuple[1]
            self.description = testInfoTuple[2]
            # self.description = ""
            # self.name = None
        self.tasksAnswered=0
        self.correctAnswers=0

    def addThisTestToALibrary(self, libraryId):
        self.lepDB.addTestIDandLibraryIDtoTesttoLibraryTableDB(self.id, libraryId)
        pass

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE
        self.lepDB.updateTestNameDB(self.id, self.name)

    def setDescription(self, newDescription):
        self.description = newDescription
        # UPDATE THE DATABASE
        self.lepDB.updateTestDescriptionDB(self.id, self.description)

    def addNewTaskAndGetId(self):
        t = Task(testId=self.id)
        self.tasks[t.getTaskId()] = t
        # UPDATE THE DATABASE (wait no the task class should manage by itself)
        return t.getTaskId()

    def addTask(self,task):
        self.tasks[task.getTaskId()] = task
        # adding a premade task instance no need for databse stuff

    def removeTask(self, taskId):
        del self.tasks[taskId]
        # UPDATE THE DATABASE
        self.lepDB.deleteTaskDB(taskId)


    def getTestId(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getTaskIds(self):
        if (self.getTasks() is None):
            return []
        return list(self.getTasks().keys())

    def getTask(self, taskId):
        if self.tasks is None:
            self.tasks = {}
            ids=self.lepDB.getTaskIDFromTestIDDB(self.id) #GET ALL THE TASK IDS FROME THE DATABASE

            for i in ids:
                self.__loadTask(i)
        return self.tasks[taskId]

    def getTasks(self):
        if self.tasks is None:
            self.tasks = {}
            ids=self.lepDB.getTaskIDFromTestIDDB(self.id) #GET ALL THE TASK IDS FROME THE DATABASE
            for i in ids:
                #print("getTasks, ",i)
                self.__loadTask(i[0])
        return self.tasks

    def __loadTask(self, taskId):
        t = Task(taskId=taskId)
        self.tasks[t.getTaskId()] = t

    def resetTest(self):
        for id, task in self.getTasks().items():
            task.removeAnswerGiven()
        self.tasksAnswered=0
        self.correctAnswers=0

    def addTaskAnswerGiven(self, taskId, answerId):
        self.tasksAnswered+=1
        task = self.tasks[taskId]
        task.addAnswerGiven(answerId)
        if task.validityOfGivenAnswer():
            self.correctAnswers+=1

    def getProgression(self):
        return [self.tasksAnswered,len(self.getTasks())]

    def getScore(self):
        return [self.correctAnswers,len(self.getTasks())]
