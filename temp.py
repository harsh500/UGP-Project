from z3 import *

def example():
    s = Solver()
    x = Int('x')
    y = Int('y')
    constraint1 = x > 10
    print(type(constraint1))
    s.add(constraint1, y == x + 2)
    print(s.assertions())  # prints the constraints added above
    print(s.check()) # check for satisfiability
    solve(s.assertions()) # prints one of the possible solutions
    