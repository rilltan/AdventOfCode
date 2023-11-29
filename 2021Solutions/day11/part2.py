import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

grid = [[int(x) for x in line] for line in data]

def flashcoord(r,c,grid,flashedgrid):
    if grid[r][c] > 9 and flashedgrid[r][c] == 0:
        flashedgrid[r][c] = 1
        for ra in incrange(-1,1):
            for ca in incrange(-1,1):
                if inbounds(r+ra, 0, len(grid)-1) and inbounds(c+ca, 0, len(grid[0])-1):
                    grid[r+ra][c+ca] += 1
                    flashcoord(r+ra,c+ca,grid,flashedgrid)
    
i = 0
flag = True
while flag:
    i+=1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1
    
    flashedgrid = [[0]*len(grid[0]) for _ in grid]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            flashcoord(r,c,grid,flashedgrid)
    
    all = True
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if flashedgrid[r][c] == 1:
                grid[r][c] = 0
            else:
                all = False
    if all:
        flag = False

print(i)