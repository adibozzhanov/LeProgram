from task import Task

class Test:
    # can either be initialized by the testId if it is already in the database
    # or by creating a new task if no id is given
    def __init__(self, testId=None):
        if testId is None:
            self.name = None
            self.description = ""
            self.tasks = {}
            self.tags = {} #we need a tag class? or what do we do with them
            # ADD A NEW TEST IN THE DATABASE
            self.id = 0 # GET THE NEW ID FROM THE DATABASE
        else:
            self.id = testId
            self.tasks = None # only create the task instances when they ate requested
            # LOAD DATA FROM THE DATABASE
            # self.description = ""
            # self.name = None
        self.tasksAnswered=0
        self.correctAnswers=0

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE

    def setDescription(self, newDescription):
        self.description = newDescription
        # UPDATE THE DATABASE

    def addTaskAndGetId(self):
        t = Task(testId=self.id)
        self.tasks[t.getTaskId()] = t
        # UPDATE THE DATABASE (wait no the task class sould manage by itself)
        return t.getTaskId()

    def removeTask(self, taskId):
        del self.tasks[taskId]
        # UPDATE THE DATABASE

    def getTestId(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getTask(self, taskId):
        if self.tasks is None:
            ids=[] #GET ALL THE ANSWER IDS FROME THE DATABASE
            for i in ids:
                self.__loadTask(i)
        return self.tasks[taskId]

    def getTasks(self):
        if self.tasks is None:
            ids=[] #GET ALL THE ANSWER IDS FROME THE DATABASE
            for i in ids:
                self.__loadTask(i)
        return self.tasks

    def __loadTask(self, taskId):
        t = Task(taskId=taskId)
        self.tasks[t.getTaskId()] = t

    def resetTest(self):
        for id, task in self.tasks.items():
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
        return [self.tasksAnswered,len(self.tasks)]

    def getScore(self):
        return [self.correctAnswers,len(self.tasks)]
