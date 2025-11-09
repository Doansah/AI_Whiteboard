from sympy import Eq
from sympy.core.backend import sympify
from sympy.parsing.latex import parse_latex


# a line is a full equation.
# for instance ->  200x - 4 = 50x -10
# for each line split left and right
#

'''
errorDict: 
    Key: index of error in solutionAttempt.lines
    Value: what went wrong
 
 '''
class Recommendation:
    def __init__(self,solutionAttempt, errorDict ):
        self.solutionAttempt = solutionAttempt
        self.errorDict = errorDict
        self.recommendationString = ""



def to_sympy(SolutionAttempt):

    lines = SolutionAttempt.getExpressions()

    for i in range (len(lines) -1 ):
        currentline = lines[i]
        left, right = currentline.split("=")

        # checking if the line is valid
        leftExpr = parse_latex(left)
        rightExpr = parse_latex(right)

        structure_equality = isEqualStructure()
        numeric_equality = isEqualNumeric(leftExpr, rightExpr)
        if structure_equality or numeric_equality:
            continue

        # validate the expression!

    else:
        return "Error: not latex, fix later"

    if "=" in line:
        leftSide, rightSide = line.split("=")
        return Eq(sympify(leftSide), sympify(rightSide))
    return sympify(line)

def isEqualStructure(leftSide, rightSide):
    return sympify(leftSide) == sympify(rightSide)

# check if sides are equal interms of number ->
def isEqualNumeric(leftSide, rightSide):
    return leftSide.equals(rightSide)

def inferOperation(currentEq :Eq, nextEq: Eq):
    isValidOperation = (nextEq.lhs - currentEq.lhs).simplify().equals(nextEq.rhs - currentEq.rhs)

    if not isValidOperation:


    # curr: 10x - 5 = 20
    # next: 10x = 15
    # operation was  MINUS 5




