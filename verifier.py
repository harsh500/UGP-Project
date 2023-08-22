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

def do_back_tracking_for_thread_parallel_version(ir,constraints,do_operate_till_index=0,start_index=None):

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
            constraints1_left = do_back_tracking_for_thread_parallel_version(
                ir,
                updated_constraints,
                i["branch_starts"][0],
                i["previous_possible_instructions"][0]
                ) 
            constraints1_right = do_back_tracking_for_thread_parallel_version(
                ir,
                updated_constraints,
                i["branch_starts"][1],
                i["previous_possible_instructions"][1]
                ) 
            if(ir[i["branch_starts"][0]-1]["instruction_type"]=="condition_on_prob"):
                j= i["branch_starts"][0]-2
                c_left = ir[j+1]["probability"]+"*("+constraints1_left+")"
                c_right = "(1-("+ir[j+1]["probability"]+"))*("+constraints1_right+")"
                print(c_left)
                print(c_right)
                updated_constraints = c_left + "+" + c_right
            if(ir[i["branch_starts"][0]-1]["instruction_type"]=="demonic_choice"):
                j= i["branch_starts"][0]-2
                updated_constraints = "If(("+constraints1_left+"<"+constraints1_left+"),"+constraints1_left+","+constraints1_right+")"
                print(updated_constraints)
        print(updated_constraints)
        print("##########END\n")
    return updated_constraints