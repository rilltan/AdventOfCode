import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x = []
id=0
for i,c in enumerate(data[0]):
    if i%2==0:
        x.extend([id] * int(c))
        id+=1
    else:
        x.extend([-1] * int(c))

groups = [(a[0],len(list(a[1]))) for a in it.groupby(x)]
pos = 0
id = len(groups)-1
file = groups[-1][0]
while id > 0:
    pos = 0
    file -= 1
    while pos<id and (groups[pos][1] < groups[id][1] or groups[pos][0] != -1):
        pos += 1
    if pos == len(groups):
        id -= 1
        while groups[id][0] == -1:
            id -= 1
        continue

    groups.insert(pos,groups[id])
    id += 1
    pos += 1
    groups[pos] = (groups[pos][0],groups[pos][1] - groups[id][1])
    groups[id] = (-1, groups[id][1])
    id -= 1
    if groups[id][0]==-1 and id<len(groups)-1 and groups[id+1][0] == -1:
        groups[id] = (-1, groups[id][1] + groups.pop(id+1)[1])
    while (groups[id][0] == -1 or groups[id][0] > file) and id > 0:
        id -= 1

i=0
out=0
for group in groups:
    if group[0] != -1:
        out += group[0] * ((group[1]+i)*(group[1]+i-1)//2 - i*(i-1)//2)
    i += group[1]

prco(out)
