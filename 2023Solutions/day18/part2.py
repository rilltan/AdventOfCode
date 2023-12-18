import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [x.split() for x in data]

dirs = {"3":(-1,0),"0":(0,1),"2":(0,-1),"1":(1,0)}

grid = [(0,0)]
perim = 0
for line in data:
    d = line[2][-2]
    num = int(line[2][2:-2],base=16)
    perim += num
    prev = grid[-1]
    grid.append((prev[0]+num*dirs[d][0],prev[1]+num*dirs[d][1]))

area = 0
for i in range(len(grid)-1):
    area += grid[i][1]*grid[i+1][0] - grid[i][0]*grid[i+1][1]
area = area//2
interior = area - (perim//2) + 1
prco(interior+perim)