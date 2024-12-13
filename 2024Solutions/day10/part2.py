import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

nines = []
grid = makegrid(len(data)+2,len(data[0])+2,-2)
for r in range(len(data)):
    for c in range(len(data[r])):
        grid[r+1][c+1] = int(data[r][c])
        if data[r][c] == "9":
            nines.append((r+1,c+1))

paths = [set()]
current_path = 0
zeroes_on_path = []
i=0
while i < len(nines):
    zeroes_on_path.append(0)
    dfs = deque()
    dfs.append(nines[i])
    while dfs:
        c = dfs.pop()
        for dir in u_cardinals:
            if grid[c[0]][c[1]] - grid[c[0]+dir[0]][c[1]+dir[1]] == 1:
                dfs.append((c[0]+dir[0],c[1]+dir[1]))
                if grid[c[0]+dir[0]][c[1]+dir[1]] == 0:
                    zeroes_on_path[current_path] += 1
    i+=1
    current_path += 1

prco(sum(zeroes_on_path[i] for i in range(len(zeroes_on_path))))