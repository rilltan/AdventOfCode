import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

ts = set(data[0].replace(" ","").split(","))
towels = data[2:]

def ans(t):
    if t in ts:
        return True
    for i in range(len(t),0,-1):
        if t[:i] in ts:
            if ans(t[i:]):
                return True
    return False

prco(sum(1 for a in towels if ans(a)))


# one line
def ans(t):
    return True if t in ts else any(ans(t[i:]) for i in range(len(t),0,-1) if t[:i] in ts)