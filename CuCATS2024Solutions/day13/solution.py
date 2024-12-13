import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

n,m,k = getints(data[0]) # num children, num frienships, num naughty, num coal

naughty = getints(data[1])

links = [getints(line) for line in data[2:2+m]]

graph = {}
for link in links:
    if link[0] not in graph:
        graph[link[0]] = []
    if link[1] not in graph:
        graph[link[1]] = []
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

def transform(childrengraph,naughtylist,numberofchildren,removed):
    naughty = 0
    allchildren = set([i for i in range(numberofchildren) if i!=removed])

    while allchildren:
        current_graph = set()
        search = deque()
        search.append(allchildren.pop())
        current_graph.add(search[0])
        while search:
            current = search.popleft()
            if current in childrengraph:
                for a in childrengraph[current]:
                    if a not in current_graph and a in childrengraph:
                        current_graph.add(a)
                        search.append(a)
                        allchildren.remove(a)
        if any([x in naughtylist for x in current_graph]):
            naughty += len(current_graph)
    
    return naughty

ans = 999999
id = 0
for i in range(n):
    if i in graph:
        vals = graph.pop(i)
        if transform(graph,naughty,n,i) <= ans:
            ans = transform(graph,naughty,n,i)
            id=i
        graph[i] = vals

prco(f"{id},{ans}")