from models.lexerParser import getExpressionTree
from models.library import Library
from models.user import User
from models.randomTaskGenerator import TaskGenerator
from models.test import Test
from models.answer import Answer
from models.task import Task
from models.expression import Expression

if __name__ == '__main__': #testing
    u = User()
    u.setName("Carmen")
    l = u.getLibrary()
    testId = l.addNewTestAndGetId()
    t = l.getTest(testId)
    t.setName("testytest")
    taskId = t.addNewTaskAndGetId()
    print(taskId)
    q = t.getTask(taskId)
    answerId = q.addNewAnswerAndGetId()
    t.addTaskAnswerGiven(taskId,answerId)
    print(t.tasksAnswered, t.correctAnswers)
    t.resetTest()
    print(t.tasksAnswered, t.correctAnswers)
    taskId = t.addNewTaskAndGetId()
    print(taskId)
    q = t.getTask(taskId)
    answerId = q.addNewAnswerAndGetId()
    a = q.getAnswer(answerId)
    a.setCorrect()
    t.addTaskAnswerGiven(taskId,answerId)
    print(t.tasksAnswered, t.correctAnswers)
    print(t.getScore())
