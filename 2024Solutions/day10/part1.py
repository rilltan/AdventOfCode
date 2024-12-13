import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

zeroes = []
grid = makegrid(len(data)+2,len(data[0])+2,-2)
for r in range(len(data)):
    for c in range(len(data[r])):
        grid[r+1][c+1] = int(data[r][c])
        if data[r][c] == "0":
            zeroes.append((r+1,c+1))

paths = [set()]
current_path = 0
zeroes_on_path = []
nines_on_path = []
i=0
while i < len(zeroes):
    zeroes_on_path.append(1)
    nines_on_path.append(0)
    dfs = deque()
    seen = set()
    dfs.append(zeroes[i])
    seen.add(zeroes[i])
    while dfs:
        c = dfs.popleft()
        for dir in u_cardinals:
            if (c[0]+dir[0],c[1]+dir[1]) not in seen and -grid[c[0]][c[1]] + grid[c[0]+dir[0]][c[1]+dir[1]] == 1:
                seen.add((c[0]+dir[0],c[1]+dir[1]))
                dfs.append((c[0]+dir[0],c[1]+dir[1]))
                if grid[c[0]+dir[0]][c[1]+dir[1]] == 0:
                    zeroes.remove((c[0]+dir[0],c[1]+dir[1]))
                    zeroes_on_path[current_path] += 1
                elif grid[c[0]+dir[0]][c[1]+dir[1]] == 9:
                    nines_on_path[current_path] += 1
    i+=1
    current_path += 1

prco(sum(zeroes_on_path[i]*nines_on_path[i] for i in range(len(zeroes_on_path))))