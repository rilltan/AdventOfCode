import math
inputfile = open("day24.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

grid3d = {}
width = len(lines[0]) - 2
height = len(lines) - 2
depth = math.lcm(width,height)
for x in range(width):
    for y in range(height):
        for z in range(depth):
            grid3d[x,y,z] = 1
for x in range(-1,width+1):
    for z in range(depth):
        grid3d[x,-1,z] = 0
        grid3d[x,height,z] = 0
for y in range(-1,height+1):
    for z in range(depth):
        grid3d[-1,y,z] = 0
        grid3d[width,y,z] = 0
blizzards = []
direction = {">":(1,0),"<":(-1,0),"v":(0,1),"^":(0,-1)}
for y,i in enumerate(lines):
    for x,j in enumerate(i):
        grid3d[x-1,y-1,0] = 1 if j=="." else 0
        if j!="#" and j!=".":
            blizzards.append([x-1,y-1,j])
grid3d[width-1,height,0] = 0
for a in range(1,depth):
    for i in range(len(blizzards)):
        blizzards[i][0] += direction[blizzards[i][2]][0]
        blizzards[i][0] %= width
        blizzards[i][1] += direction[blizzards[i][2]][1]
        blizzards[i][1] %= height
        grid3d[blizzards[i][0],blizzards[i][1],a] = 0

nodes = {}
next = ((0,0),(1,0),(-1,0),(0,1),(0,-1))
for z in range(depth):
    for y in range(height):
        for x in range(width):
            if grid3d[x,y,z]:
                connected = set()
                for xnext,ynext in next:
                    if grid3d[x+xnext,y+ynext,(z+1)%depth]:
                        connected.add((x+xnext,y+ynext,(z+1)%depth))
                nodes[x,y,z] = set(connected)
    connected = set()
    connected.add((0,-1,(z+1)%depth))
    if grid3d[0,0,(z+1)%depth]:
        connected.add((0,0,(z+1)%depth))
    nodes[0,-1,z] = set(connected)
    connected = set()
    connected.add((width-1,height,(z+1)%depth))
    if grid3d[width-1,height-1,(z+1)%depth]:
        connected.add((width-1,height-1,(z+1)%depth))
    nodes[width-1,height,z] = set(connected)

for z in range(depth):
    if (width-1,height-1,z) in nodes:
        connected = set(nodes[width-1,height-1,z])
        connected.add((width-1,height,(z+1)%depth))
        nodes[width-1,height-1,z] = set(connected)
    if (0,0,z) in nodes:
        connected = set(nodes[0,0,z])
        connected.add((0,-1,(z+1)%depth))
        nodes[0,0,z] = set(connected)

def bfs(start,end):
    global nodes
    distances = {a:10000 for a in nodes}
    distances[start] = 0
    visited = set()
    queue = [start]

    while queue:
        x = queue.pop(0)
        if x not in visited:
            visited.add(x)
            for child in nodes[x]:
                if child not in visited:
                    distances[child] = distances[x]+1
                    if child[0] == end[0] and child[1] == end[1]:
                        return(distances[child])
                    else:
                        queue.append(child)

first = bfs((0,-1,0),(width-1,height))
second = bfs((width-1,height,first%depth),(0,-1))
third = bfs((0,-1,(first+second)%depth),(width-1,height))
print(first+second+third)