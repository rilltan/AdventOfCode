import os
import sys
import itertools as it
import random
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

graph = {}
componentset = set()
for line in data:
    l = line.replace(":","").split(" ")
    for w in l:
        componentset.add(w)
    if l[0] not in graph:
        graph[l[0]] = []
    graph[l[0]].extend(l[1:])
    for wire in l[1:]:
        if wire not in graph:
            graph[wire] = []
        graph[wire].append(l[0])
components = list(componentset)

def findpath(nodes):
    start = nodes[0]
    end = nodes[1]
    q = deque([start])
    paths = {}
    currentitem = start
    while currentitem != end:
        for component in graph[currentitem]:
            if component not in paths:
                paths[component] = currentitem
                q.append(component)
        currentitem = q.popleft()
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
        currentitem = q.popleft()
        for component in graph[currentitem]:
            if any((component==cuts[i][0] and currentitem==cuts[i][1]) or (component==cuts[i][1] and currentitem == cuts[i][0]) for i in range(len(cuts))):
                continue
            if component not in seen:
                seen.add(component)
                q.append(component)
    return seen

def bfscuts(cuts):
    start = cuts[0][0]
    q = deque()
    seen = set()
    q.append(start)
    seen.add(start)
    while q:
        currentitem = q.popleft()
        for component in graph[currentitem]:
            if any((component==cuts[i][0] and currentitem==cuts[i][1]) or (component==cuts[i][1] and currentitem == cuts[i][0]) for i in range(len(cuts))):
                continue
            if component not in seen:
                seen.add(component)
                q.append(component)
        if cuts[0][1] in seen:
            return False
    return seen

def findgroups(cuts):
    group = bfscuts(cuts)
    if group and len(group) != len(components):
        return len(group)*(len(components)-len(group))
    return -1


counts = {}
for i in range(500):
    for wire in findpath(random.sample(components,2)):
        if wire == -1:
            continue
        if wire not in counts:
            counts[wire] = 0
        counts[wire] += 1

wires = [(x,y) for x,y in counts.items()]
wires.sort(key=lambda x:x[1],reverse=True)
wires = [x[0] for x in wires]
wires = [x for x in wires if type(x)!=str]
for cuts in it.combinations(wires[:3],3):
    result = findgroups(cuts)
    if result != -1:
        print(result)
        break