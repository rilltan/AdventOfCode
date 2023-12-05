import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [getints(x) for x in data]
seeds = data[0]

mapped = set()
for i,seedmap in enumerate(data[1::]):
    if not seedmap:
        mapped = set()
    else:
        for j in range(len(seeds)):
            if inbounds(seeds[j],seedmap[1],seedmap[1]+seedmap[2]-1) and j not in mapped:
                mapped.add(j)
                seeds[j] += seedmap[0] - seedmap[1]

prco(min(seeds))