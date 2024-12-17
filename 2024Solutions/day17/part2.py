import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def possibilities(program):
    poss = []
    for i,n in enumerate(program):
        poss.append([])
        for j in range(8):
            a = (n^1^j) << (j^2)
            r = 7 << (j^2)
            if (j&7&r) ^ (a&7&r) == 0:
                poss[i].append(((j|a)<<3*i, (7|r)<<3*i))
        poss[i] = sorted(poss[i],key=lambda x:x[0])
    
    return poss[::-1]

def dfs(poss,current,required_bits,level):
    if level == len(poss):
        return current
    for n in poss[level]:
        if (n[0] & required_bits & n[1]) ^ (current & required_bits & n[1]) == 0:
            num = dfs(poss,n[0]|current, required_bits|n[1], level+1)
            if num != -1:
                return num
    return -1

prco(dfs(possibilities(getints(data[4])),0,0,0))
