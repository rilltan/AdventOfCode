import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
import functools

ts = set(data[0].replace(" ","").split(","))
towels = data[2:]

@functools.lru_cache(None)
def ans(t):
    ways = 0
    if t == "":
        return 1
    for i in range(1,len(t)+1):
        if t[:i] in ts:
            ways += ans(t[i:])
    return ways

prco(sum(ans(a) for a in towels))


# one line
@functools.lru_cache(None)
def ans(t):
    return 1 if t == "" else sum(ans(t[i:]) for i in range(1,len(t)+1) if t[:i] in ts)