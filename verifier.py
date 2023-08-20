import copy
from z3 import *
from helpers import * 

def do_back_tracking_for_thread(ir,constraints,do_operate_till_index=0,start_index=None):

    j=start_index
    if j==None:
        j=len(ir)-1
    print("DO BACK TRACKING CALLED ",do_operate_till_index,j)
    updated_constraints = copy.deepcopy(constraints)
    while j>=do_operate_till_index:
        i = ir[j]
        if i["instruction_type"]=="assignment":
            updated_constraints = updated_constraints.replace(i["lhs"],"("+i["rhs"]+")")
        print(i)
        if(len(i["previous_possible_instructions"]))==1:
            j=i["previous_possible_instructions"][0]
        else:
            constraints1_left = do_back_tracking_for_thread(
                ir,
                updated_constraints,
                i["branch_starts"][0],
                i["previous_possible_instructions"][0]
                ) 
            constraints1_right = do_back_tracking_for_thread(
                ir,
                updated_constraints,
                i["branch_starts"][1],
                i["previous_possible_instructions"][1]
                ) 
            j= i["branch_starts"][0]-2
            c_left = "And("+ir[j+1]["condition"]+","+constraints1_left+")"
            c_right = "And(Not("+ir[j+1]["condition"]+"),"+constraints1_right+")"
            print(c_left)
            print(c_right)
            updated_constraints = "Or("+c_left+","+c_right+")"
            # updated_constraints = "Or(("+ir[j+1]["condition"]+","+constraints1_left+"),(Not("+ir[j+1]["condition"]+"),"+constraints1_right+"))"
        print("\n\n######START")
        print(updated_constraints)
        print("##########END\n")    
            # updated_constraints = "Or"
        

    print(updated_constraints)
    return updated_constraints
    # addConstraint("Or(x>=0,x<0)",s)
    # for i in reversed(ir):
    #     print(i)
    #     addAssignment(i["lhs"],i["rhs"])
    # print(getVar('y'))
    # print(s)
    # print(s.simplify())