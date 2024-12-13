import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "^":
            a=(i,j)


dirs = [(-1,0),(0,1),(1,0),(0,-1)]
d=0
visited = set()

while inbounds(a[0],1,len(data)-2) and inbounds(a[1],1,len(data[0])-2):
    if data[a[0]+dirs[d][0]][a[1]+dirs[d][1]]!="#":
        a = (a[0]+dirs[d][0],a[1]+dirs[d][1])
    else:
        d=(1+d)%4
        a=(a[0]+dirs[d][0],a[1]+dirs[d][1])
    visited.add(a)

prco(len(visited))