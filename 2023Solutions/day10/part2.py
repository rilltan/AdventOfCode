import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

dirs = {"|":((1,0),(-1,0)),"-":((0,1),(0,-1)),"L":((-1,0),(0,1)),"J":((-1,0),(0,-1)),"7":((1,0),(0,-1)),"F":((1,0),(0,1))}

for r,line in enumerate(data):
    for c,letter in enumerate(line):
        if letter == "S":
            start = (r,c)

found = False
i=-1
while not found:
    i+=1
    path = [start,(start[0]+u_cardinals[i][0],start[1]+u_cardinals[i][1])]
    currentpipe = data[path[-1][0]][path[-1][1]]
    if currentpipe not in dirs:
        continue
    if (-u_cardinals[i][0],-u_cardinals[i][1]) not in dirs[currentpipe]:
        continue

    searching = True
    while searching:
        currentpipe = data[path[-1][0]][path[-1][1]]
        searching = False
        if currentpipe in dirs:
            for r,c in dirs[currentpipe]:
                if path[-1][0]+r != path[-2][0] or path[-1][1]+c!=path[-2][1]:
                    nextpipe = data[path[-1][0]+r][path[-1][1]+c]
                    if nextpipe == "S":
                        found = True
                        break
                    elif nextpipe in dirs and (-r,-c) in dirs[nextpipe]:
                        path.append((path[-1][0]+r,path[-1][1]+c))
                        searching = True
                        break

bigpath = set()
for i in range(-1,len(path)-1):
    bigpath.add((path[i][0]*2,path[i][1]*2))
    bigpath.add((path[i][0]+path[i+1][0],path[i][1]+path[i+1][1]))
gridsize = (max(x[0] for x in bigpath)+1,max(x[1] for x in bigpath)+1)

floodset = set((0,0))
flood = [(0,0)]
i = 0
while i<len(flood):
    for r,c in u_cardinals:
        new = (flood[i][0]+r,flood[i][1]+c)
        if new not in floodset and new not in bigpath and inbounds(new[0],-1,gridsize[0]) and inbounds(new[1],-1,gridsize[1]):
            flood.append(new)
            floodset.add(new)
    i+=1

result = 0
for r in range(0,gridsize[0]+1,2):
    for c in range(0,gridsize[1]+1,2):
        if (r,c) not in floodset and (r,c) not in bigpath:
            result += 1

prco(result)