import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

n,m,k,c = getints(data[0]) # num children, num frienships, num naughty, num coal

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

# print(graph)
# print(naughty)

nice_connections = {x:0 for x in naughty}
naughty_connections = {x:0 for x in naughty}
for id in naughty:
    if id not in graph:
        continue
    search = deque()
    seen = set()
    search.append(id)
    seen.add(id)
    while search:
        current = search.popleft()
        for a in graph[current]:
            if a not in seen:
                seen.add(a)
                search.append(a)
                if a in naughty:
                    naughty_connections[id] += 1
                else:
                    nice_connections[id] += 1
    print(f"########{id}")
    print(seen)
    print(naughty_connections[id])
    print(nice_connections[id])

print(naughty_connections)
print(nice_connections)

na = sorted([(a,naughty_connections[a],nice_connections[a]) for a in naughty],key=lambda x:x[1],reverse=True)
for a in na:
    print(a)
print()
for x in na:
    if x[2] != 14 and x[2]>0:
        print(x)
print()
print(c)

for y in [136,9,40,124,53,78,49]:
    nums = sorted([x for x in naughty if nice_connections[x]==14] + [y])
    print(len(nums))
    for num in nums:
        print(num,end=",")
    print()