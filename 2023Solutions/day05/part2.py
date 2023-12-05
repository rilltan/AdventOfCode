import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [getints(x) for x in data]
seedranges = []
for i in range(len(data[0])//2):
    seedranges.append((data[0][i*2],data[0][i*2]+data[0][i*2+1]-1))
seedmaps = [[]]
j=0
for x in data[1::]:
    if x:
        seedmaps[j].append(x)
    else:
        j+=1
        seedmaps.append([])
seedmaps = [x for x in seedmaps if x]
seedmaps = [sorted(x,key=lambda y:y[1]) for x in seedmaps]

print(seedmaps)
print(seedranges)

for maptype in seedmaps:
    newranges = []
    print(seedranges)
    for srange in seedranges:
        sources = [(x[1],x[1]+x[2]-1) for x in maptype]
        #print(sources)
        if srange[0] < sources[0][0]:
            newranges.append((srange[0],sources[0][0]-1))
        for smap in maptype:
            if srange[0] <= smap[1]+smap[2]-1 and srange[1] >= smap[1]:
                newranges.append((max(srange[0],smap[1])+smap[0]-smap[1],min(srange[1],smap[1]+smap[2]-1)+smap[0]-smap[1]))
        if srange[1] > sources[-1][1]:
            newranges.append((sources[-1][1]+1,srange[1]))
    seedranges = [x for x in newranges]