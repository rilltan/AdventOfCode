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
seens = [set([start,(start[0]-1,start[1])]),set([start,(start[0],start[1]+1)])]
while all(x!=end for x in points):
    newpoints = []
    flag = True
    lengths = [0 for _ in points]
    turns = [[] for _ in points]
    while flag:
        flag = False
        for i in range(len(points)):
            p = points[i]
            d = dirs[i]
            samedir = False
            if data[p[0]+d[0]][p[1]+d[1]] != "#":
                points[i] = (p[0]+d[0],p[1]+d[1])
                scores[i] += 1
                lengths[i] += 1
                seen.add((p[0]+d[0],p[1]+d[1]))
                seens[i].add((p[0]+d[0],p[1]+d[1]))
                samedir = True
                flag = True
            di = dirs[i]
            for d in u_cardinals:
                if (p[0]+d[0],p[1]+d[1]) not in seen and data[p[0]+d[0]][p[1]+d[1]] != "#":
                    newpoints.append((p[0]+d[0],p[1]+d[1]))
                    dirs.append(d)
                    seens.append(set(seens[i]))
                    if samedir:
                        scores.append(scores[i]+1000)
                        seens[-1].remove((p[0]+di[0],p[1]+di[1]))
                    else:
                        scores.append(scores[i]+1001)
                    seens[-1].add((p[0]+d[0],p[1]+d[1]))
                    seen.add((p[0]+d[0],p[1]+d[1]))
                    turns[i].append(len(dirs)-1)
    toremove = []
    for i,j in it.combinations(range(len(points)),2):
        if points[i] == points[j]:
            if scores[i] == scores[j]:
                seens[i] = seens[i].union(seens[j])
                toremove.append(j)
                if lengths[i]<lengths[j]:
                    shorter = i
                    longer=  j
                else:
                    shorter = j
                    longer = i
                for turn in turns[shorter]:
                    seens[turn] = seens[turn].union(seens[i])
                    turnloc = (newpoints[turn-len(points)][0] - dirs[turn][0],newpoints[turn-len(points)][1]-dirs[turn][1])
                    if points[i][0] == turnloc[0] and points[i][1] < turnloc[1]:
                        for k in incrange(turnloc[1]-1,points[i][1]):
                            seens[turn].remove((points[i][0],k))
                    elif points[i][0] == turnloc[0] and points[i][1] > turnloc[1]:
                        for k in incrange(turnloc[1]+1,points[i][1]):
                            seens[turn].remove((points[i][0],k))
                    elif points[i][1] == turnloc[1] and points[i][0] < turnloc[0]:
                        for k in incrange(turnloc[0]-1,points[i][0]):
                            seens[turn].remove((k,points[i][1]))
                    elif points[i][1] == turnloc[1] and points[i][0] > turnloc[0]:
                        for k in incrange(turnloc[0]+1,points[i][0]):
                            seens[turn].remove((k,points[i][1]))
            else:
                if scores[i] < scores[j]:
                    toremove.append(j)
                    for turn in turns[j]:
                        toremove.append(turn)
                else:
                    toremove.append(i)
                    for turn in turns[i]:
                        toremove.append(turn)
    toremove = sorted(toremove,reverse=True)
    points = points + newpoints
    for i in toremove:
        points.pop(i)
        dirs.pop(i)
        scores.pop(i)
        seens.pop(i)

index = points.index(end)
prco(len(seens[index]))