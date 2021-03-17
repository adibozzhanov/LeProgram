from answer import Answer

# using answer ids to reference them or something like the index? as in their order in the task

class Task:
    # can either be initialized by the taskId if it is already in the database
    # or by giving the testID to create a new task
    def __init__(self, testId=None, taskId=None):
        if taskId is None:
            self.testId = testId
            self.statement = ""
            self.expression = None
            self.answers = {}
            # ADD A NEW TASK IN THE DATABASE



            # OOO WAIT UNLESS testId IS NONE CAUSE THEN IT IS A RANDOMLY GENERATED TEST AND WE DO NOT NEED IT!
            self.id = 0 # GET THE NEW ID FROM THE DATABASE
            # if testID is none dont bother with database and ID
        else:
            self.id = taskId
            self.answers = None # only when requested
            # LOAD DATA FROM THE DATABASE
            # self.testId = testId
            # self.statement = ""
            # self.expression = None
        self.answerGivenId = None

    def setExpression(self, newExpression):
        self.expression = (newExpression)
        # UPDATE THE DATABASE

    def setExpressionFromTree(self, newExpressionTree):
        self.expression = Expression(newExpressionTree)
        # UPDATE THE DATABASE

    def setStatement(self, newStatement):
        self.statement = newStatement
        # UPDATE THE DATABASE

    def addNewAnswerAndGetId(self):
        a = Answer(taskId=self.id)
        self.answers[a.getAnswerId()] = a
        # UPDATE THE DATABASE (wait not the answer class will do that anyway)
        return a.getAnswerId()

    def addAnswer(self,a):
        self.answers[a.getAnswerId()] = a
        # adding a premade answer instance no need for databse stuff

    def removeAnswer(self, answerId):
        del self.answers[answerId]
        # UPDATE THE DATABASE

    def getTaskId(self):
        return self.id

    def getTestId(self): # not sure if needed
        return self.testId

    def getExpression(self):
        return self.expression

    def getStatement(self):
        return self.statement

    def getAnswer(self, answerId):
        if self.answers is None:
            ids=[] #GET ALL THE ANSWER IDS FROME THE DATABASE
            for i in ids:
                self.__loadAnswer(i)
        return self.answers[answerId]

    def getAnswers(self):
        if self.answers is None:
            ids=[] #GET ALL THE ANSWER IDS FROME THE DATABASE
            for i in ids:
                self.__loadAnswer(i)
        return self.answers

    def __loadAnswer(self, answerId):
        a = Answer(answerId=answerId)
        self.answers[a.getAnswerId()] = a

    def addAnswerGiven(self, answerId):
        self.answerGivenId = answerId

    def getAnswerGiven(self):
        return self.answers[self.answerGivenId]

    def removeAnswerGiven(self):
        self.answerGivenId = None

    def validityOfGivenAnswer(self):
        a = self.getAnswerGiven()
        if a is None: return None
        return a.getIsCorrect()
