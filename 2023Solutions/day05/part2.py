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
i=0
for x in data[1::]:
    if x:
        seedmaps[i].append(x)
    else:
        i+=1
        seedmaps.append([])
seedmaps = [x for x in seedmaps if x]
seedmaps = [sorted(x,key=lambda y:y[1]) for x in seedmaps]

for seedmapgroup in seedmaps:
    newranges = []
    for srange in seedranges:
        sources = [(x[1],x[1]+x[2]-1) for x in seedmapgroup]
        transforms = [x[0]-x[1] for x in seedmapgroup]

        if srange[0] < sources[0][0]:
            newranges.append((srange[0], min(sources[0][0]-1,srange[1])))
        for i,source in enumerate(sources):
            if srange[0] <= source[1] and srange[1] >= source[0]:
                newranges.append((max(srange[0],source[0])+transforms[i], min(srange[1],source[1])+transforms[i]))
        if srange[1] > sources[-1][1]:
            newranges.append((max(sources[-1][1]+1,srange[0]), srange[1]))
        
    seedranges = [x for x in newranges]

prco(min([x[0] for x in seedranges]))