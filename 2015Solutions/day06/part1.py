import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

grid = makegrid(1000,1000,False)

for line in data:
    r1,c1,r2,c2 = getints(line)
    if line[6] == "n":
        for r in incrange(r1,r2):
            for c in incrange(c1,c2):
                grid[r][c] = True
    elif line[6] == "f":
        for r in incrange(r1,r2):
            for c in incrange(c1,c2):
                grid[r][c] = False
    else:
        for r in incrange(r1,r2):
            for c in incrange(c1,c2):
                grid[r][c] = not grid[r][c]

prco(sum(sum(row) for row in grid))