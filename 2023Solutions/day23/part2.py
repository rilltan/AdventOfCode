import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

dirs = {"<":(0,-1),">":(0,1),"v":(1,0),"^":(-1,0)}

junctions = []
junctions.append((0,1))
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c]==".":
            count = 0
            for ra,ca in u_cardinals:
                if not inbounds(r+ra,0,len(data)-1) or not inbounds(c+ca,0,len(data)-1):
                    continue
                if data[r+ra][c+ca] in dirs:
                    count += 1
            if count > 1:
                junctions.append((r,c))
junctions.append((len(data)-1,len(data[0])-2))

graph = {i:[] for i in range(len(junctions)-1)}

for i in range(len(junctions)-1):
    for ra,ca in u_cardinals:
        r = junctions[i][0]
        c = junctions[i][1]
        path = [(r,c),(r+ra,c+ca)]
        found = False
        while not found:
            r = path[-1][0]
            c = path[-1][1]
            stepped = False
            for rb,cb in u_cardinals:
                if not inbounds(r+ra,0,len(data)-1) or not inbounds(c+ca,0,len(data)-1):
                    continue
                if data[r+rb][c+cb] != "#" and (r+rb,c+cb) != path[-2]:
                    stepped = True
                    path.append((r+rb,c+cb))
                    break
            if not stepped:
                found = True
            if (data[path[-2][0]][path[-2][1]] in dirs or path[-1][0]==len(data)-1) and path[-1] in junctions:
                graph[i].append((junctions.index(path[-1]),len(path)-1))
                found = True

seen = set()
def dfs(index,path,longest):
    global seen
    
    if index == len(junctions) - 1:
        if path > longest:
            print(path)
        return path

    for node in graph[index]:
        if node[0] not in seen:
            seen.add(node[0])
            longest = max(longest,dfs(node[0],path+node[1],longest))
            seen.remove(node[0])
    return longest

prco(dfs(0,0,0))

# Currently takes about 1 minute to run, will improve later