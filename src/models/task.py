import Expression
import Answer

# using answer ids to reference them or something like the index? as in their order in the task

class Task:
    counter = 0
    # can either be initialized by the taskId if it is already in the database
    # or by giving the testID to create a new task
    def __init__(self, testId=None, taskId=None):
        if not taskId:
            self.id = counter
            counter+=1
            self.testId = testId
            self.statement = ""
            self.expression = None
            self.answers = {}
            # ADD A NEW TASK IN THE DATABASE
        else:
            self.id = taskId
            # LOAD DATA FROM THE DATABASE
            # self.testId = testId
            # self.statement = ""
            # self.expression = None
            # self.answers = []

    def setExpression(self, newExpressionTree):
        self.expression = Expression(newExpressionTree)
        # UPDATE THE DATABASE

    def setStatement(self, newStatement):
        self.statement = newStatement
        # UPDATE THE DATABASE

    def addAnswerAndGetId(self):
        a = Answer(taskId=self.id)
        self.answers[a.getAnswerId()] = a
        # UPDATE THE DATABASE
        return a.getAnswerId()

    def removeAnswer(self, answerId):
        del self.answers[answerId]
        # UPDATE THE DATABASE

    def getTaskId(self):
        return self.id

    def getTestId(self): # not sure if needed
        return self.testId

    def getExpression(self):
        return self.expression

    def getAnswerIds(self): #either keep the following 2 or the one after them
        return list(self.answers)

    def getAnswer(self, answerId):
        return self.answers[answerId]

    def getAnswers(self, answerId):
        return self.answers
