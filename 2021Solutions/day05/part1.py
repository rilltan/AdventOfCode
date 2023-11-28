import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [getints(x) for x in data]
maximum = max(flatten(data))
grid = makegrid(maximum+1,maximum+1, 0)


for line in data:
    if line[0]==line[2] or line[1] == line[3]:
        for c in range(min(line[0],line[2]),max(line[0],line[2])+1):
            for r in range(min(line[1],line[3]),max(line[1],line[3])+1):
                grid[c][r] += 1


result = 0
for num in flatten(grid):
    if num > 1:
        result += 1

print(result)