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
        exec("global %s; %s = Real(\"%s\")"%(i,i,i))

    s = Solver()
    if(data["program_type"][0]=="probabilistic"):
        p1_1 = do_back_tracking_for_thread_parallel_version(data["Q"]["T1"],data["R"])
        given_cond=data["P"][0]
        f2 = open("debug.txt","w")
        f2.write(p1_1)
        final= given_cond + " < " + p1_1
        final=eval(final)
        print("-------------------------")
        print(final)
        print("-------------------------")
        s.add(final)
        if(s.check()==sat):
            print("The given proof is wrong and counter example is: ")
            print(s.model())
        else:
            print("The given proof is correct")  
    if(data["program_type"][0]=="non-probabilistic"):
        p1_1 = do_back_tracking_for_thread(data["Q"]["T1"],data["R"])
        print(p1_1)
        f2 = open("debug.txt","w")
        f2.write(p1_1)
        given_cond="True"
        for cond in data["P"]:
            given_cond="And("+given_cond+","+cond+")"
        final="And("+p1_1+",Not("+given_cond+"))"
        final=eval(final)
        s.add(final)
        print(s.assertions())
        if(s.check()==sat):
            print("The given proof is wrong and counter example is: ")
            print(s.model())
        else:
            print("The given proof is correct")
