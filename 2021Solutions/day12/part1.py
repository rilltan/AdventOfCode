import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

graph = {}
for a,b in [x.split("-") for x in data]:
    if a not in graph:
        graph[a] = list()
    graph[a].append(b)

    if b not in graph:
        graph[b] = list()
    graph[b].append(a)

def dfs(graph, visited = ["start"]):
    paths = 0
    if visited[-1] == "end":
        return 1
    else:
        for x in graph[visited[-1]]:
            if x.isupper():
                new = [y for y in visited]
                new.append(x)
                paths += dfs(graph,new)
            elif x not in visited and x != "start":
                new = [y for y in visited]
                new.append(x)
                paths += dfs(graph,new)
        return paths

prco(dfs(graph))