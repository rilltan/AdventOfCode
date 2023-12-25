import os
import sys
import itertools as it
import random
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

wires = {}
wireset = set()
for line in data:
    l = line.replace(":","").split(" ")
    for w in l:
        wireset.add(w)
    if l[0] not in wires:
        wires[l[0]] = []
    wires[l[0]].extend(l[1:])
    for edge in l[1:]:
        if edge not in wires:
            wires[edge] = []
        wires[edge].append(l[0])
wirelist = list(wireset)

def findpath(nodes):
    start = nodes[0]
    end = nodes[1]
    q = deque([start])
    paths = {}
    pos = start
    while pos != end:
        for wire in wires[pos]:
            if wire not in paths:
                paths[wire] = pos
                q.append(wire)
        pos = q.popleft()
    path = []
    done = False
    while not done:
        path.append(tuple(sorted((end,paths[end]))))
        if paths[end] == start:
            done = True
        end = paths[end]
    return path

def bfs(start,cuts):
    q = deque()
    seen = set()
    q.append(start)
    seen.add(start)
    while q:
        pos = q.popleft()
        for wire in wires[pos]:
            if any((wire==cuts[i][0] and pos==cuts[i][1]) or (wire==cuts[i][1] and pos == cuts[i][0]) for i in range(len(cuts))):
                continue
            if wire not in seen:
                seen.add(wire)
                q.append(wire)
    return seen

def bfscuts(cuts):
    start = cuts[0][0]
    q = deque()
    seen = set()
    q.append(start)
    seen.add(start)
    while q:
        pos = q.popleft()
        for wire in wires[pos]:
            if any((wire==cuts[i][0] and pos==cuts[i][1]) or (wire==cuts[i][1] and pos == cuts[i][0]) for i in range(len(cuts))):
                continue
            if wire not in seen:
                seen.add(wire)
                q.append(wire)
        if cuts[0][1] in seen:
            return False
    return seen

def findgroups(cuts):
    group1 = bfscuts(cuts)
    if group1 and len(group1) != len(wireset):
        return len(group1)*(len(wireset)-len(group1))
    return -1


counts = {}
for i in range(500):
    for edge in findpath(random.sample(wirelist,2)):
        if edge == -1:
            continue
        if edge not in counts:
            counts[edge] = 0
        counts[edge] += 1

items = [(x,y) for x,y in counts.items()]
items.sort(key=lambda x:x[1],reverse=True)
items = [x[0] for x in items]
items = [x for x in items if type(x)!=str]
for cuts in it.combinations(items[:10],3):
    result = findgroups(cuts)
    if result != -1:
        print(result)
        break