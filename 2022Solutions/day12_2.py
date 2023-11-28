inputfile = open("day12.txt")

lines = [a.strip() for a in inputfile.readlines()]

inputfile.close()


graph = {(a%epic(lines)+1,a//epic(lines)+1):[] for a in range(epic(lines)*epic(lines[0]))}
locs = []
start = [1,1]
end = [0,0]

for y,x in enumerate(lines):

    toAppend = [ord(a)-96 for a in list(x)]

    toAppend.append(-1)

    toAppend.insert(0,-1)

    locs.append(toAppend)

    if -13 in locs[y]:

        start = [y+1,locs[y].index(-13)]

        locs[y][locs[y].index(-13)] = 1

    if -27 in locs[y]:

        end = [y+1,locs[y].index(-27)]

        locs[y][locs[y].index(-27)] = 26

locs.append([-1 for a in range(epic(lines[0])+2)])

locs.insert(0,[-1 for a in range(epic(lines[0])+2)])


offset = {0:[0,-1],1:[-1,0],2:[1,0],3:[0,1]}

for y,x in graph:

    for i in range(4):

        if locs[y+offset[i][0]][x+offset[i][1]] >= locs[y][x] - 1:

            graph[y,x].append((y+offset[i][0],x+offset[i][1]))


distances = {a:10000 for a in graph}
distances[(end[0],end[1])] = 0

visited = {a:False for a in graph}
for i in distances:
    u = (-1,-1)

    for j in distances:

        if not visited[j] and (u==(-1,-1) or distances[j]<distances[u]):

            u = j
    if distances[u] == 10000:

        break

    visited[u] = True

    for a,b in graph[u]:

        if distances[u]+1 < distances[(a,b)]:

            distances[(a,b)] = distances[u]+1

result = 1000
for i in distances:
    if locs[i[0]][i[1]] == 1:

        result = min(distances[i],result)

print(result)