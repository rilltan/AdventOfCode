import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [getints(x) for x in data]
seeds = data[0]

seedmap = {}
for i,x in enumerate(data[1::]):
    if not x:
        mapped = set()
    else:
        for j in range(len(seeds)):
            if inbounds(seeds[j],x[1],x[1]+x[2]-1) and j not in mapped:
                if j == 1:
                    print(x)
                mapped.add(j)
                seeds[j] += -x[1]+x[0]

        print(seeds)
prco(min(seeds))