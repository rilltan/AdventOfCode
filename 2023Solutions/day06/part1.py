import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

times = getints(data[0])
dists = getints(data[1])

result = 1
for i in range(len(times)):
    ways = 0
    for j in range(times[i]):
        if j * (times[i]-j) > dists[i]:
            ways += 1
    result *= ways

prco(result)