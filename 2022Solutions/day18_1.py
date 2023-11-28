inputfile = open("day18.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

grid = {}
for x in lines:
  x = x.split(",")
  grid[int(x[0]),int(x[1]),int(x[2])] = 1

check = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
area = 0
for i in grid:
    for j in check:
        tocheck = (i[0]+j[0],i[1]+j[1],i[2]+j[2])
        if tocheck not in grid:
            area += 1
print(area)