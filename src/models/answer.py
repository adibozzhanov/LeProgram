from expression import Expression
from database import Database

# the expression tree should be passed from the controller after it parsed the input

class Answer:
    # can either be initialized by the answerId if it is already in the database
    # or by giving the taskID to create a new answer
    def __init__(self, taskId=None, answerId=None):

        database = Database()

        if answerId is None:
            self.taskId = taskId
            self.expression = None
            self.isCorrect = False
            # ADD A NEW ANSWER TO THE DATABASE
            self.id = 0 # GET THE NEW ID FROM THE DATABASE
        else:
            self.id = answerId
            # LOAD THE 3 VARIABLES FROM THE DATABASE
            #self.isCorrect = False
            #self.taskId = taskId
            #self.expression = Expression(expressionTree)

    def setExpression(self, newExpressionTree):
        self.expression = Expression(newExpressionTree)
        # UPDATE THE DATABASE

    def setCorrect(self):
        self.isCorrect = True
        # UPDATE THE DATABASE

    def setIncorrect(self):
        self.isCorrect = False
        # UPDATE THE DATABASE

    def getAnswerId(self):
        return self.id

    def getTaskId(self): #not sure if needed
        return self.taskId

    def getExpression(self):
        return self.expression

    def getIsCorrect(self):
        return self.isCorrect
