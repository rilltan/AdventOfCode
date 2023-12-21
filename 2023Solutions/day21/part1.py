import os
import sys
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

start = (-1,-1)
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "S":
            start = (r,c)

q = deque()
q.append(start)
num = 1
seen = set()
for i in range(64):
    newnum = 0
    seen.clear()
    for j in range(num):
        pos = q.popleft()
        for r,c in u_cardinals:
            if (pos[0]+r,pos[1]+c) not in seen and inbounds(pos[0]+r,0,len(data)-1) and inbounds(pos[1]+c,0,len(data[0])-1) and data[pos[0]+r][pos[1]+c] != "#":
                seen.add((pos[0]+r,pos[1]+c))
                q.append((pos[0]+r,pos[1]+c))
                newnum += 1
    num = newnum

prco(len(q))