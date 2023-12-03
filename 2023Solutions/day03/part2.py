import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

grid = {}
gridunique = {}
for r in range(len(data)):
    count = 0
    prev = False
    ints = [abs(x) for x in getints(data[r])]
    for c in range(len(data[0])):
        if re.match(r"\d",data[r][c]):
            grid[(r,c)] = ints[count]
            gridunique[(r,c)] = (r,count)
            prev = True
        elif prev:
            count += 1
            prev = False

result = 0
added = set()
for r in range(len(data)):
    for c in range(len(data[0])):
        if re.match(r"[^\w.]",data[r][c]):
            num = 0
            ratio = 1
            for ra,ca in u_adjacent:
                if (r+ra,c+ca) in grid and gridunique[r+ra,c+ca] not in added:
                    num += 1
                    added.add(gridunique[r+ra,c+ca])
                    ratio *= grid[r+ra,c+ca]
            if num == 2:
                result += ratio

prco(result)