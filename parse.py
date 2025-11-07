from sympy import Eq
from sympy.core.backend import sympify
from sympy.parsing.latex import parse_latex


# a line is a full equation for instance: 200x - 4 = 50x -10
# for each line split left and right
#
def to_sympy(line:str, isLatex:bool):
    if not isLatex:
        # Converts the input LaTeX string ``s`` to a SymPy ``Expr``
        return parse_latex(line)
    else:
        return "Error: not latex, fix later"

    if "=" in line:
        leftSide, rightSide = line.split("=")
        return Eq(sympify(leftSide), sympify(rightSide))
    return sympify(line)

def bothSidesEqualStructure(leftSide, rightSide):
    return sympify(leftSide) == sympify(rightSide)

# check if sides are equal interms of number ->
def bothSidesEqualNumeric(leftSide, rightSide):


