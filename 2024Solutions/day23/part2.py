import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

graph = {}
for line in data:
    x,y = line.split("-")
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)

groups = set([tuple([x]) for x in graph])
while len(groups)>1:
    newgroups = set()
    for g in groups:
        for d in graph[g[0]]:
            if d not in g:
                if all(d in graph[a] for a in g):
                    newgroups.add(tuple(sorted(list(g) + [d])))
    groups = newgroups

prco(",".join(groups.pop()))