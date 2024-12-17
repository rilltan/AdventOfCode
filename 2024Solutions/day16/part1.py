import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

start = (len(data)-2,1)
end = (1,len(data[0])-2)

seen = set()
points = [(start[0]-1,start[1]),(start[0],start[1]+1)]
dirs = [(-1,0),(0,1)]
scores = [1001,1]
while all(x!=end for x in points):
    newpoints = []
    flag = True
    while flag:
        flag = False
        for i in range(len(points)):
            p = points[i]
            d = dirs[i]
            samedir = False
            if (p[0]+d[0],p[1]+d[1]) not in seen and data[p[0]+d[0]][p[1]+d[1]] != "#":
                points[i] = (p[0]+d[0],p[1]+d[1])
                scores[i] += 1
                seen.add((p[0]+d[0],p[1]+d[1]))
                samedir = True
                flag = True
            for d in u_cardinals:
                if (p[0]+d[0],p[1]+d[1]) not in seen and data[p[0]+d[0]][p[1]+d[1]] != "#":
                    newpoints.append((p[0]+d[0],p[1]+d[1]))
                    dirs.append(d)
                    if samedir:
                        scores.append(scores[i]+1000)
                    else:
                        scores.append(scores[i]+1001)
                    seen.add((p[0]+d[0],p[1]+d[1]))
    points = points + newpoints

index = points.index(end)
prco(scores[index])