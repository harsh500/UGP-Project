import sys
import json

from z3 import  *
from temp import example
from helpers import * 
from verifier import *

solver_variable_mappings = {}

if __name__ == '__main__':

    print("[LOG] Started the program")

    n = len(sys.argv)
    if n<2:
        print("[ERROR] Input file name required")
        sys.exit()

    input_file = sys.argv[1]
    print(n,input_file)

    f = open(input_file)
    data = json.load(f)

    for i in data["variables_used"]:
        add_new_z3_variable(i)
        # print(type(i))

    s = Solver()

    # for i in data["R"]:
    #     addConstraint(i,s)

    print(s.assertions())

    p1_1 = do_back_tracking_for_thread(data["Q"]["T1"],data["R"])
    print(p1_1)
    f2 = open("debug.txt","w")
    f2.write(p1_1)
    
    addConstraint(p1_1,s)
    # p2_2 = do_back_tracking_for_thread(data["Q"]["T2"],data["R"])
    # for i in p1_1:
    #     addConstraint(i,s)
    # for i in p2_2:
    #     addConstraint(i,s)
    print(s.assertions())
    print("wdfvyqegydqevyfy\n\n\n\n\n")
    print(solve(s.assertions()))

    

    # solver_variable_mappings = precompute()
    # # print(convert_assignment_to_z3(data["T1"][0]["lhs"],data["T1"][0]["rhs1"],solver_variable_mappings))
    # print(convert_assignment_to_z3(data["T1"][1]["lhs"],data["T1"][1]["rhs1"],solver_variable_mappings,data["T1"][1]["operator"],data["T1"][1]["rhs2"]))
    # z= convert_assignment_to_z3(data["T1"][1]["lhs"],data["T1"][1]["rhs1"],solver_variable_mappings,data["T1"][1]["operator"],data["T1"][1]["rhs2"])
    # s = Solver()
    # s.add(z)
    # solve(s.assertions())
    # print("DSFDGRF")
    # example()    


