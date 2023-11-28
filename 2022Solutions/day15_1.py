inputfile = open("day15.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

sensors = {}
coverage = []
count=0
for x in lines:
    x = x.replace(",","")
    x = x.replace(":","")
    x = x.split(" ")
    a = int(x[2].split("=")[1])
    b = int(x[3].split("=")[1])
    c = int(x[8].split("=")[1])
    d = int(x[9].split("=")[1])
    sensors[(a,b)] = (c,d)

for x,y in sensors:
    distx = abs(x-sensors[x,y][0])
    disty = abs(y-sensors[x,y][1])
    dist = distx+disty
    j=10
    currentdist = abs(j-y)
    amount = dist-currentdist
    coverage.append((x-amount,x+amount))

count = set([])
for x1,x2 in coverage:
    temp = set(range(x1,x2))
    count = count.union(temp)
print(len(count))