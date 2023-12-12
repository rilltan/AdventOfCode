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
    if len(pattern) < sum(lengths):
        return 0
    if pattern[0] == "?":
        return possibilites("."+pattern[1:],lengths) + possibilites("#"+pattern[1:],lengths)
    if re.match(f"[?#]{{{lengths[0]}}}([?.]|$)",pattern):
        return possibilites(pattern[lengths[0]+1:],lengths[1:]) 
    return 0

result = 0
for line in data:
    result += possibilites("?".join(line.split()[0] for i in range(5)),tuple(getints(line))*5)

prco(result)