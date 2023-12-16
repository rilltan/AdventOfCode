import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

reflect = {"\\":{"E":"S","S":"E","W":"N","N":"W"},"/":{"E":"N","N":"E","S":"W","W":"S"}}
visited = set()
result = set()
rays = [["E",0,0]]
stop = False
while not stop:
    length = len(rays)
    stop = True
    for i in range(length):
        dir = rays[i][0]
        c = rays[i][1]
        r = rays[i][2]
        if not dir:
            continue
        if not inbounds(c,0,len(data[0])-1) or not inbounds(r,0,len(data)-1):
            rays[i][0] = ""
            continue
        if (dir,c,r) in visited:
            rays[i][0] = ""
            continue
        stop = False

        visited.add((dir,c,r))
        result.add((c,r))
        if data[r][c] in reflect:
            rays[i][0] = reflect[data[r][c]][dir]
        elif data[r][c] == "|" and dir!="S" and dir!="N":
            rays[i][0] = "S"
            rays.append(["N",c,r-1])
        elif data[r][c] == "-" and dir!="E" and dir!="W":
            rays[i][0] = "E"
            rays.append(["W",c-1,r])
        rays[i][1] += u_dirs[rays[i][0]][0]
        rays[i][2] += u_dirs[rays[i][0]][1]

prco(len(result))