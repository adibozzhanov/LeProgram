from expression import Expression

# the expression tree should be passed from the controller after it parsed the input

class Answer:
    counter = 0
    # can either be initialized by the answerId if it is already in the database
    # or by giving the taskID to create a new answer
    def __init__(self, taskId=None, answerId=None):
        if not answerId:
            self.id = counter
            counter+=1
            self.taskId = taskId
            self.expression = None
            self.isCorrect = False
            # ADD A NEW ANSWER IN THE DATABASE
        else:
            self.id = answerId
            # LOAD THE 3 VARIABLES FROM THE DATABASE
            #self.isCorrect = False
            #self.taskId = taskId
            #self.expression = Expression(expressionTree)

    def updateExpression(self, newExpressionTree):
        self.expression = Expression(newExpressionTree)
        # UPDATE THE DATABASE

    def makeCorrect(self):
        self.isCorrect = True
        # UPDATE THE DATABASE

    def makeIncorrect(self):
        self.isCorrect = False
        # UPDATE THE DATABASE

    
