import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

dirs = {"|":((1,0),(-1,0)),"-":((0,1),(0,-1)),"L":((-1,0),(0,1)),"J":((-1,0),(0,-1)),"7":((1,0),(0,-1)),"F":((1,0),(0,1)),"S":u_cardinals}

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

prco(len(path)//2)