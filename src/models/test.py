import Expression
import Answer

class Test:
    counter = 0
    # can either be initialized by the testId if it is already in the database
    # or by creating a new task if no id is given
    def __init__(self, testId=None):
        if not testId:
            self.id = counter
            counter+=1
            self.name = None
            self.description = ""
            self.tasks = {}
            self.tags = {} #we need a tag class? or what do we do with them
            # ADD A NEW TEST IN THE DATABASE
        else:
            self.id = testId
            # LOAD DATA FROM THE DATABASE
            # self.testId = testId
            # self.statement = ""
            # self.expression = None
            # self.answers = []

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE

    def setDescription(self, newDescription):
        self.description = newDescription
        # UPDATE THE DATABASE

    def addTaskAndGetId(self):
        t = Task(testId=self.id)
        self.tasks[t.getTaskId()] = t
        # UPDATE THE DATABASE
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
