import os
import sys
import itertools as it
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [getints(x) for x in data]
maximum = max(flatten(data))
grid = makegrid(maximum+1,maximum+1, 0)

for line in data:
    if line[0]==line[2]:
        for c,r in it.zip_longest(incrange(line[0],line[2]),incrange(line[1],line[3]),fillvalue=line[0]):
            grid[c][r] += 1
    elif line[1]==line[3]:
        for c,r in it.zip_longest(incrange(line[0],line[2]),incrange(line[1],line[3]),fillvalue=line[1]):
            grid[c][r] += 1
    else:
        for c,r in zip(incrange(line[0],line[2]),incrange(line[1],line[3])):
            grid[c][r] += 1


result = 0
for num in flatten(grid):
    if num > 1:
        result += 1

print(result)