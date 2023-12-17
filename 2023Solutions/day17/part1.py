import os
import sys
import heapq
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

reverse = {"N":"S","S":"N","E":"W","W":"E","":""}

visited = set()
queue = [(0,0,0,"",0)] # (distance,row,column,direction,straight line distace)
heapq.heapify(queue)
result = 100000
while queue:
    current = heapq.heappop(queue)

    if (current[1],current[2],current[3],current[4]) not in visited:
        visited.add((current[1],current[2],current[3],current[4]))

        for d in u_dirs:
            if d==reverse[current[3]]:
                continue

            if d == current[3]:
                straight = current[4] + 1
                if straight > 3:
                    continue
            else:
                straight = 1

            r = current[1]+u_dirs[d][0]
            c = current[2]+u_dirs[d][1]
            if r == len(data)-1 and c == len(data[0])-1:
                result = min(current[0] + int(data[r][c]), result)
                continue
            if inbounds(r,0,len(data)-1) and inbounds(c,0,len(data[0])-1):
                heapq.heappush(queue,(current[0] + int(data[r][c]),r,c,d,straight))

prco(result)