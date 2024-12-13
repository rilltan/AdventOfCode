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
gaps = sum(a[1] for a in groups if a[0] == -1)
pos = 0
while gaps > 0:
    while groups[pos][0] != -1:
        pos += 1
    num = min(groups[-1][1], groups[pos][1])
    groups[pos] = (groups[pos][0],groups[pos][1] - num)
    groups.insert(pos,(groups[-1][0], num))
    groups[-1] = (groups[-1][0],groups[-1][1] - num)
    gaps -= num
    pos+=1

    if groups[-1][1] == 0:
        groups.pop()
        if groups[-1][0] == -1:
            gaps -= groups.pop()[1]
    if groups[pos][1] == 0:
        gaps -= groups.pop(pos)[1]
        
i=0
out=0
for group in groups:
    out += group[0] * ((group[1]+i)*(group[1]+i-1)//2 - i*(i-1)//2)
    i += group[1]

prco(out)