import random
from models.lexerParser import Node, getExpressionTree
from models.task import Task
from models.test import Test
from models.expression import Expression
from models.answer import Answer

#Question templates will be programmed into the application. Examples include:
#-Which of the following expressions is equivalent to this logical DNF?
#   create une expression and its dnf and then just make sure that the other random ones do not have the same tt
#-Which is the correct DNF form of this logical expression?
#   same as previous but just output other values
#-Which of the following is a valid/invalid expression?
#-Which of the following is satisfiable/unsatisfiable?
#   maybe just generate one and make sure that the other ones are not the same..
#... or just do not give a fuck and allow for multiple answers

class TestGenerator:
    # NB WHEN DISPLAYING THE TASK MAKE THE ORDER OF TASKS RANDOM AT SOME POINT CAUSE RN EVERY FIRST ANSWER IS THE CORRECT ONE!
    nrOfAnswers = 4
    probabilityOfNot = 0.2
    binaryOp = ['and','or','xor','imp','iff']
    notOp = 'not'
    values = ['top','bot']
    def __init__(self, complexity = 3, LibraryId = 1, amountOfTasks = 25):
        self.complexity = complexity
        self.LibraryId = LibraryId
        self.amountOfTasks = amountOfTasks
        self.variables = ['top','bot']
        self.nrOfVariables = min(int(3+(complexity-3)/4),complexity)
        self.unsatisfiableAnswers = []
        self.validAnswers = []
        self.__generateVariables()
        self.tasksAnswered=0
        self.correctAnswers=0

    def getTest(self):
        test = Test()
        test.addThisTestToALibrary(self.LibraryId)
        for t in range(self.amountOfTasks):
            test.addTask(self.__getTask(test))
        return test


    def __getTask(self, test):
        t = Task(testId = test.getTestId())
        self.__generateTask(t)
        return t

    def __addTaskAnswerGiven(self, task, answerId):
        self.tasksAnswered+=1
        task.addAnswerGiven(answerId)
        if task.validityOfGivenAnswer():
            self.correctAnswers+=1

    def __getScore(self):
        return [self.correctAnswers,self.tasksAnswered]

    def __generateTask(self, task): #PLZ IGNORE HOW POORLY THIS IS DONE RN!!!!
        a = self.__generateCorrectAnswer(task)
        answers = [a]
        if a.getExpression().getValid():
            for i in range(1,type(self).nrOfAnswers):
                answers.append(self.__generateIncorrectAnswer(a.getExpression(),task))
            self.__taskFindValid(task)
        elif not a.getExpression().getSatisfiable():
            for i in range(1,type(self).nrOfAnswers):
                answers.append(self.__generateIncorrectAnswer(a.getExpression(),task))
            self.__taskFindUnsatisfiable(task)
        else:
            if len(self.validAnswers)>=type(self).nrOfAnswers-1:
                for i in range(1,type(self).nrOfAnswers):
                    answerNotInDB = self.validAnswers.pop()
                    answerInDB = Answer(task.getTaskId())
                    answerInDB.setExpression(answerNotInDB.getExpression())
                    answers.append(answerInDB)
                self.__taskFindInvalid(task)
            elif len(self.unsatisfiableAnswers)>=type(self).nrOfAnswers-1:
                for i in range(1,type(self).nrOfAnswers):
                    answerNotInDB = self.unsatisfiableAnswers.pop()
                    answerInDB = Answer(task.getTaskId())
                    answerInDB.setExpression(answerNotInDB.getExpression())
                    answers.append(answerInDB)
                self.__taskFindSatisfiable(task)
            else:
                for i in range(1,type(self).nrOfAnswers):
                    answers.append(self.__generateIncorrectAnswer(a.getExpression(),task))
                self.__taskFindExpressionOfDNF(task, answers)
        for a in answers:
            task.addAnswer(a)
        #print("invalid ",len(self.validAnswers))
        #print("satisfiable",len(self.unsatisfiableAnswers))

    def __taskFindValid(self, task):
        task.setStatement("Which of the following is a valid expression?")

    def __taskFindUnsatisfiable(self, task):
        task.setStatement("Which of the following is an unsatisfiable expression?")

    def __taskFindInvalid(self, task):
        task.setStatement("Which of the following is an invalid expression?")

    def __taskFindSatisfiable(self, task):
        task.setStatement("Which of the following is a satisfiable expression?")

    #def __taskFindDNF(self):pass #make answers to POSSIBLY be strings too?

    def __taskFindExpressionOfDNF(self, task, answers):
        task.setStatement("Which of the following is equivalent to this DNF?\nDNF: " + answers[0].getExpression().getDNF())



    def __generateCorrectAnswer(self, task):
        _ = getExpressionTree(self.__generateExpressionString())
        ex = Expression(_)
        a = Answer(task.getTaskId())
        a.setExpression(ex)
        a.setCorrect()
        return a

    def __generateIncorrectAnswer(self, correctExpression, task):
        a = Answer(task.getTaskId())
        a.setIncorrect()
        while True:
            _ = getExpressionTree(self.__generateExpressionString())
            ex = Expression(_)
            if ex.getValid():
                a.setExpression(ex)
                self.validAnswers.append(a)
                continue
            if not ex.getSatisfiable():
                a.setExpression(ex)
                self.unsatisfiableAnswers.append(a)
                continue
            if ex.getSimpleTable() != correctExpression.getSimpleTable():
                break
        a.setExpression(ex)
        return a

    def __generateVariables(self):
        for i in range(self.nrOfVariables):
            self.variables.append(chr(ord('a') + i))

    def __generateExpressionString(self):
        var = self.variables[2:]
        while len(var)<=self.complexity:
            var.append(random.choice(self.variables))
        random.shuffle(var)
        return self.__generateOperations(self.complexity, var)

    def __generateOperations(self, c, var):
        if c == 0:
            ex = var.pop()
        else:
            split = random.randrange(c)
            ex1 = self.__generateOperations(split, var)
            ex2 = self.__generateOperations(c-1-split, var)
            ex = "("+ ex1 + random.choice(type(self).binaryOp) + ex2 +")"
        if random.random()<type(self).probabilityOfNot:
            ex = type(self).notOp + ex
        return ex



if __name__ == '__main__': #testing
    t = TestGenerator()
    test = t.getTest()
    test.setName("Carmens Big Brain "+ str(test.getTestId()))



# generate the correct answers
# if valid: ask to find valid
# if unsatisfiable: ask to find unsatisfiable
# else:
#   if enough valid or unsatisfiable (wrong answers) then ask to find invalid/satisfiable
#   generate more answers that do not have the same tt!
#       if either valid or unsatisfiable then save for later
# else make a q about dfs


# .getTableFinalColumn to compare if the expressions are the same
