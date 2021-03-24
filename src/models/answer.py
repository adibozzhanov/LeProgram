from models.expression import Expression
from models.database import Database

# the expression tree should be passed from the controller after it parsed the input

class Answer:
    # can either be initialized by the answerId if it is already in the database
    # or by giving the taskID to create a new answer
    counter=0
    def __init__(self, taskId=None, answerId=None):

        self.lepDB = Database()

        if answerId is None:

            self.taskId = taskId
            self.expression = None
            self.isCorrect = False
            # ADD A NEW ANSWER TO THE DATABASE
            self.id = self.lepDB.addNewAnswerDB(self.taskId)

            # OOO WAIT UNLESS taskId IS NONE CAUSE THEN IT IS A RANDOMLY GENERATED TEST AND WE DO NOT NEED IT!
            #self.id = 0 # GET THE NEW ID FROM THE DATABASE
            if taskId is None: #no need to put int in a database but still needs an id to function during the test taking
                self.id = type(self).counter
                type(self).counter=type(self).counter%100+1


        else:
            self.id = answerId
            # LOAD THE 3 VARIABLES FROM THE DATABASE
            answerInfoTuple = self.lepDB.loadAnswerDB(answerId)
            self.taskId = answerInfoTuple[1]
            self.setExpression(answerInfoTuple[2])
            if answerInfoTuple[3] == 0:
                self.isCorrect = False
            else:
                self.isCorrect = True

            #self.isCorrect = False
            #self.taskId = taskId
            #self.expression = Expression(expressionTree)

    def setExpression(self, newExpression):
        self.expression = (newExpression)
        # UPDATE THE DATABASE
        self.lepDB.updateAnswerExp(self.id, self.expression)

    def setExpressionFromTree(self, newExpressionTree):
        self.expression = Expression(newExpressionTree)
        # UPDATE THE DATABASE
        self.lepDB.updateAnswerExp(self.id, self.expression.getString())

    def setCorrect(self):
        self.isCorrect = True
        # UPDATE THE DATABASE
        self.lepDB.updateIsCorrect(self.id, 1)


    def setIncorrect(self):
        self.isCorrect = False
        # UPDATE THE DATABASE
        self.lepDB.updateIsCorrect(self.id, 0)


    def getAnswerId(self):
        return self.id

    def getTaskId(self): #not sure if needed
        return self.taskId

    def getExpression(self):
        return self.expression

    def getIsCorrect(self):
        return self.isCorrect
