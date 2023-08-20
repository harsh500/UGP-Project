from z3 import *

def add_new_z3_variable(x):
    exec("global %s; %s = Int(\"%s\")"%(x,x,x))

def addConstraint(constraint,s):
    exec("s.add(%s)"%(constraint))

def addAssignment(lhs,rhs):
    exec("global %s;%s=%s"%(lhs,lhs,rhs))

def getVar(var):
    _locals = locals()
    print(_locals)
    exec("exp = %s"%(var),globals(),_locals)
    exp = _locals['exp']
    return exp
    
def precompute():
    return {
        "x":Int('x'),
        "y":Int('y')
        # "c":Int('a'),
        # "d":Int('a'),
        # "e":Int('a'),
        # "f":Int('a'),
        # "g":Int('a'),
        # "h":Int('a'),
        # "i":Int('a'),
        # "j":Int('a'),
        # "k":Int('a'),
        # "l":Int('a'),
        # "m":Int('a'),
        # "n":Int('a'),
        # "o":Int('a'),
        # "":Int('a'),
        # "a":Int('a'),
        # "a":Int('a'),
        
    }

def convert_assignment_to_z3(lhs,rhs1,vars,operator=None,rhs2=None):
    if operator is not None and rhs2 is None:
        print("[ERROR] invalid format")
        sys.exit()
    if operator is None:
        lhs_updated = convert_all_to_z3(lhs,vars)
        rhs_updated = convert_all_to_z3(rhs1,vars)
        e= lhs_updated = rhs_updated
        return e
    else:
        lhs_updated = convert_all_to_z3(lhs,vars)
        rhs1_updated = convert_all_to_z3(rhs1,vars)
        rhs2_updated = convert_all_to_z3(rhs2,vars)
        if operator == "+":
            e = lhs_updated ==rhs1_updated + rhs2_updated
            return e 
        elif operator==">":
            lhs_updated = convert_all_to_z3(lhs,vars)
            rhs1_updated = convert_all_to_z3(rhs1,vars)
            e =  lhs_updated > rhs1_updated
            return e
        print("[ERROR] invalid format")
        sys.exit()
    

def convert_all_to_z3(s,vars):
    if s in vars.keys():
        return vars[s]
    return s

    