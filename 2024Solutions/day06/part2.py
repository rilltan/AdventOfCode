import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

visited=set()
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "^":
            start=(i,j)
data[start[0]] = data[start[0]][:start[1]] + "." + data[start[0]][start[1]+1:]

d=0
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

a=start
while inbounds(a[0],1,len(data)-2) and inbounds(a[1],1,len(data[0])-2):
    while data[a[0]+dirs[d][0]][a[1]+dirs[d][1]] == "#":
        d=(1+d)%4
    a=(a[0]+dirs[d][0],a[1]+dirs[d][1])
    visited.add(a)

loop = 0
for loc in visited:
    if loc == start:
        continue

    data[loc[0]] = data[loc[0]][:loc[1]] + "#" + data[loc[0]][loc[1]+1:]

    states = set()
    d=0
    a = start
    while inbounds(a[0],1,len(data)-2) and inbounds(a[1],1,len(data[0])-2):
        while data[a[0]+dirs[d][0]][a[1]+dirs[d][1]] == "#":
            d=(1+d)%4
        a=(a[0]+dirs[d][0],a[1]+dirs[d][1])
        x = len(states)
        states.add((a,d))
        if x == len(states):
            loop += 1
            break
    
    data[loc[0]] = data[loc[0]][:loc[1]] + "." + data[loc[0]][loc[1]+1:]

prco(loop)