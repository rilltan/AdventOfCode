import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [x.split() for x in data]

grid = [(0,0)]
perim = 0
for line in data:
    d = line[0]
    num = int(line[1])
    prev = grid[-1]
    perim += num
    grid.append((prev[0]+num*u_dirsLR[d][0],prev[1]+num*u_dirsLR[d][1]))

area = 0
for i in range(len(grid)-1):
    area += grid[i][1]*grid[i+1][0] - grid[i][0]*grid[i+1][1]
area = area//2
interior = area - (perim//2) + 1
prco(interior+perim)