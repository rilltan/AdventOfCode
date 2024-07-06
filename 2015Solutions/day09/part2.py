import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
import itertools as it
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

size = 1
while data[size].split()[0] == data[size-1].split()[0]:
    size += 1
size += 1
graph = makegrid(size,size,-1)

r = 0
c = 0
for line in data:
    distance = int(line.split()[4])
    c += 1
    if c >= size:
        r += 1
        c = r+1
    graph[r][c] = distance
    graph[c][r] = distance

best = 0
for steps in it.permutations(range(size),size):
    distance = sum(graph[steps[i]][steps[i+1]] for i in range(size-1))
    best = max(best,distance)

prco(best)