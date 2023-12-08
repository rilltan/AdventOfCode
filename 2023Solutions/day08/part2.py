import os
import sys
import re,math
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

steps = data[0]
network = [re.findall(r"[A-Z0-9]+",x) for x in data[2:]]
graph = {x:(y,z) for x,y,z in network}
dirs = {"R":1,"L":0}

startnodes = [x for x in graph if x[2]=="A"]
pathstoZ = []
for i,start in enumerate(startnodes):
    j = 1
    pathstoZ.append([graph[start][dirs[steps[0]]]])
    while pathstoZ[i][-1][2] != "Z":
        pathstoZ[i].append(graph[pathstoZ[i][-1]][dirs[steps[j%len(steps)]]])
        j+=1

Zdists=[len(x) for x in pathstoZ]
prco(math.lcm(*Zdists))