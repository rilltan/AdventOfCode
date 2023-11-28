inputfile = open("day15.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

sensors = {}
sizes = {}
for x in lines:
    x = x.replace(",", "")
    x = x.replace(":", "")
    x = x.split(" ")
    a = int(x[2].split("=")[1])
    b = int(x[3].split("=")[1])
    c = int(x[8].split("=")[1])
    d = int(x[9].split("=")[1])
    sensors[a, b] = (c, d)

for x, y in sensors:
    distx = abs(x - sensors[x, y][0])
    disty = abs(y - sensors[x, y][1])
    dist = distx + disty
    sizes[x, y] = dist

tocheck = []
index = 0
for middlex, middley in sensors:
    tocheck.append({})
    x = middlex
    y = middley - sizes[middlex, middley] - 1
    for i in range(sizes[middlex, middley] + 2):
        if x >= 0 and y >= 0 and x <= 4000000 and y <= 4000000:
            tocheck[index][x, y] = True
        x += 1
        y += 1
    index += 1
    print(middlex)
print()
checkagainst = []
index = 0
for middlex, middley in sensors:
    checkagainst.append({})
    x = middlex
    y = middley - sizes[middlex, middley] - 1
    for i in range(sizes[middlex, middley] + 2):
        if x >= 0 and y >= 0 and x <= 4000000 and y <= 4000000:
            checkagainst[index][x, y] = True
        x -= 1
        y += 1
    x += 1
    y -= 1
    for i in range(sizes[middlex, middley] + 1):
        if x >= 0 and y >= 0 and x <= 4000000 and y <= 4000000:
            checkagainst[index][x, y] = True
        x += 1
        y += 1
    for i in range(sizes[middlex, middley] + 2):
        if x >= 0 and y >= 0 and x <= 4000000 and y <= 4000000:
            checkagainst[index][x, y] = True
        x += 1
        y -= 1
    index += 1
    print(middlex)
overlap = 0
found = False
i = 0
while not found and i < len(tocheck):
    print(i)
    for a in tocheck[i]:
        overlap = 0
        for b in range(0, i):
            if a in checkagainst[b]:
                overlap += 1
        for b in range(i + 1, len(checkagainst)):
            if a in checkagainst[b]:
                overlap += 1
        if overlap == 4 or overlap == 3:
            found = True
            result = a[0]*4000000+a[1]
    i += 1
print()
print("Result:",result)
