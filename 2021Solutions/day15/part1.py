import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

grid = [[int(c) for c in r] for r in data]

paths = makegrid(len(grid),len(grid[0]),-1)
possible = {0:[(0,0)]}
lowest = -1

while paths[len(grid)-1][len(grid[0])-1] == -1:
    while lowest not in possible or not possible[lowest]:
        lowest += 1
    
    r,c = possible[lowest].pop(0)
    if paths[r][c] == -1:
        paths[r][c] = lowest
        for r1,c1 in u_cardinals:
            if 0<=r+r1<len(grid) and 0<=c+c1<len(grid[0]):
                if paths[r][c] + grid[r+r1][c+c1] not in possible:
                    possible[paths[r][c] + grid[r+r1][c+c1]] = []
                possible[paths[r][c] + grid[r+r1][c+c1]].append((r+r1,c+c1))
    


prco(paths[len(grid)-1][len(grid[0])-1])