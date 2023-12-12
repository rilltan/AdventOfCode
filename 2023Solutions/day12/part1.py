import os
import sys
import functools
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

@functools.cache
def possibilites(pattern,lengths):
    pattern = pattern.strip(".")
    if len(lengths)==0:
        if "#" in pattern:
            return 0
        return 1
    if not pattern:
        if len(lengths)==0:
            return 1
        else:
            return 0
    if len(pattern) < sum(lengths):
        return 0
    if pattern[0] == "?":
        return possibilites("."+pattern[1:],lengths) + possibilites("#"+pattern[1:],lengths)
    elif pattern[0] == "#":
        for i in range(lengths[0]):
            if pattern[i] == ".":
                return 0
        if len(pattern)==lengths[0]:
            return 1
        if pattern[lengths[0]] == "#":
            return 0
        return possibilites(pattern[lengths[0]+1:],lengths[1:])
        

result = 0
for line in data:
    result += possibilites(line.split()[0],tuple(getints(line)))

prco(result)