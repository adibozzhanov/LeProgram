from library import Library

class User:
    counter = 0
    def __init__(self, userId=None):
        if userId is None:
            self.id = type(self).counter
            type(self).counter+=1
            self.name = None
            self.library = Library()
            # ADD A NEW LIB IN THE DATABASE
        else:
            self.id = userId
            # LOAD DATA FROM THE DATABASE

    def setName(self, newName):
        self.name = newName
        # UPDATE THE DATABASE

    def getName(self):
        return self.name

    def getLibrary(self):
        return self.library

    def getUserId(self):
        return self.id


if __name__ == '__main__': #testing
    if True:
        u = User()
        u.setName("Carmen")
        l = u.getLibrary()
        testId = l.addTestAndGetId()
        t = l.getTest(testId)
        t.setName("testytest")
        taskId = t.addTaskAndGetId()
        print(taskId)
        q = t.getTask(taskId)
        answerId = q.addAnswerAndGetId()
        t.addTaskAnswerGiven(taskId,answerId)
        print(t.tasksAnswered, t.correctAnswers)
        t.resetTest()
        print(t.tasksAnswered, t.correctAnswers)
        taskId = t.addTaskAndGetId()
        print(taskId)
        q = t.getTask(taskId)
        answerId = q.addAnswerAndGetId()
        a = q.getAnswer(answerId)
        a.setCorrect()
        t.addTaskAnswerGiven(taskId,answerId)
        print(t.tasksAnswered, t.correctAnswers)
