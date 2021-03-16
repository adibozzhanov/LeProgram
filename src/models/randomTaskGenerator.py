import random
from parser import Node, getExpressionTree
from expression import Expression


#Question templates will be programmed into the application. Examples include:
#-Which of the following expressions is equivalent to this logical DNF?
#   create une expression and its dnf and then just make sure that the other random ones do not have the same tt
#-Which is the correct DNF form of this logical expression?
#   same as previous but just output other values
#-Which of the following is a valid/invalid expression?
#-Which of the following is satisfiable/unsatisfiable?
#   maybe just generate one and make sure that the other ones are not the same..
#... or just do not give a fuck and allow for multiple answers

class TaskGenerator:
    nrOfAnswers = 4
    probabilityOfNot = 0.3
    binaryOp = ['/AND','/OR','/XOR','/IMP','/IFF']
    notOp = '/NOT'
    values = ['/TOP','/BOT']
    def __init__(self, complexity):
        self.complexity = complexity
        self.variables = ['/TOP','/BOT']
        self.nrOfVariables = min(int(3+(complexity-3)/3),complexity)
        self.unsatisfiableExpressions = []
        self.validExpressions= []
        self.__generateVariables()



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

    def test(self):
        text = self.__generateExpressionString()
        print(text)
        tree = getExpressionTree(text)
        ex = Expression(tree)
        print("-"*20, "THE EXPRESSION:")
        print("ex: ",ex.getString())
        print("ex: ",ex.getDisplayString())
        print("-"*20, "SIMPLIFIED TABLE:")
        ex.printSimpleTable()

if __name__ == '__main__':
    g = TaskGenerator(4)
    g.test()

# generate the correct answers
# if valid: ask to find valid
# if unsatisfiable: ask to find unsatisfiable
# else:
#   generate more answers that do not have the same tt!
#       if either valid or unsatisfiable then save for later
# if enough valid or unsatisfiable (wrong answers) then ask to find invalid/satisfiable
# else make a q about dfs


# genreate the correct answer, and then more that fave a diff tt
# if valid ask whih is valid
# if not satisfiable as which is not satisfiable
# if at least half(round up) of the other answers are valid:
    # ask to pick an invalid one (might be multiple correct ones)
# if at least half of the other answers are unsatisfiable
    # ask to pick a satisfiable one (might be multiple correct ones)
#





# .getTableFinalColumn to compare if the expressions are the same
