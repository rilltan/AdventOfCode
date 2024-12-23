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

r = 0
for a,b,c in it.combinations(graph.keys(),3):
    if "t" == a[0] or "t" == b[0] or "t" == c[0]:
        if b in graph[a] and c in graph[a] and b in graph[c]:
            r += 1

prco(r)