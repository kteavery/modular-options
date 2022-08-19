import numpy as np
import os

def diverse_density():
    pass

def influence():
    pass

def most_visited(dirname):
    # first visitation frequency
    # count up the number of times a state is visited in one game
    # by matching up the state jsons for each of the (10?) runs
    # https://ai.stackexchange.com/questions/27500/why-is-it-that-the-state-visitation-frequency-equals-the-sum-of-state-visitation
    
    trials = len(next(os.walk(dirname))[1])
    counts = {}

    for i in range(trials): 
        print(dirname+"/"+str(i))
        for filename in os.listdir(dirname+"/"+str(i)):
            state = load_json(filename)
            prefix = filename.split('_')[0]
            counts[prefix+"_0"] = 1
            if i<9:
                for k in range(i+1, trials):
                    for comparefile in os.listdir(dirname+"/"+str(k)):
                        if prefix == comparefile.split('_')[0]: # filters out most comparisons
                            comparestate = load_json(comparefile)
                            if state == comparestate: 
                                counts[filename.split('_')[0]+"_0"] += 1

