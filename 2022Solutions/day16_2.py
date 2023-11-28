import itertools

inputfile = open("day16.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

flows = {}
tunnels = {}

for x in lines:
    x = x.replace("="," ")
    x = x.replace(";","")
    x = x.split(" ")
    flows[x[1]] = int(x[5])
    tunnels[x[1]] = []
    for i in range(10,len(x)):
        tunnels[x[1]].append(x[i].replace(",",""))

nodes = {a:flows[a] for a in flows if flows[a] != 0 or a == "AA"}
distanceMatrix = {b:{a:0 for a in nodes} for b in nodes}

for room in nodes:
    distances = {a:100 for a in tunnels}
    distances[room] = 0
    visited = {a:False for a in tunnels}

    for i in distances:
        u = "##"
        for j in distances:
            if not visited[j] and (u=="##" or distances[j]<distances[u]):
                u = j
        if distances[u] == 100:
            break
        visited[u] = True
        for a in tunnels[u]:
            if distances[u]+1 < distances[a]:
                distances[a] = distances[u]+1
    for i in distances:
        if i in nodes:
            distanceMatrix[room][i] = distances[i]

def calculatePressure(path):
    time = 26
    output = 0
    for i in range(1,len(path)):
        time = time - distanceMatrix[path[i-1]][path[i]] - 1
        output += time * nodes[path[i]]
    return output

def generatePaths(path):
    if path[0]>26 or len(path)-1>=len(nodes):
        return [path]
    else:
        temp = [list(path) for a in nodes]
        for index,node in enumerate(nodes):
            if node not in path and temp[index][0]+distanceMatrix[temp[index][-1]][node]+1<=26:
                temp[index].append(node)
                temp[index][0] += distanceMatrix[temp[index][-1]][temp[index][-2]]+1
            else:
                temp[index] = "##"
        i = 0
        length = len(temp)
        while i < length:
            if temp[i] == "##":
                temp.pop(i)
                i-=1
                length-=1
            i+=1
        if temp == []:
            return [path]
        for i in range(len(temp)):
            temp[i] = [a for a in generatePaths(temp[i])]
        return list(itertools.chain(*temp))

possibilites = generatePaths([0,"AA"])
best = 0
best2 = 0
bestpath = []
for i in possibilites:
    i.pop(0)
    pressure = calculatePressure(i)
    if pressure>=best:
        best=pressure
        bestpath=i
for i in possibilites:
    pressure = calculatePressure(i)
    i.pop(0)
    if pressure>best2:
        dissimilar = True
        for j in i:
            if j in bestpath:
                dissimilar = False
        if dissimilar:
            best2 = pressure

print(best+best2)