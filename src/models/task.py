import Expression
import Answer

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
            self.answers = []
            # ADD A NEW TASK IN THE DATABASE
        else:
            self.id = taskId
            # LOAD DATA FROM THE DATABASE
            # self.testId = testId
            # self.statement = ""
            # self.expression = None
            # self.answers = []

    def updateExpression(self, newExpressionTree):
        self.expression = Expression(newExpressionTree)
        # UPDATE THE DATABASE

    def addAnswer(self):
        self.answers.append(Answer(taskId=self.id))
