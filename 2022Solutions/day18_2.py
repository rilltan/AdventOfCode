inputfile = open("day18.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

grid = {}
for x in lines:
  x = x.split(",")
  grid[int(x[0]),int(x[1]),int(x[2])] = 1

water = {}
check = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
area = 0
boundsLow = (min([a for a,b,c in grid])-1,min([b for a,b,c in grid])-1,min([b for a,b,c in grid])-1)
boundsHigh = (max([a for a,b,c in grid])+1,max([b for a,b,c in grid])+1,max([c for a,b,c in grid])+1)
water[boundsLow[0],boundsLow[1],boundsLow[2]] = 1
waterToFlow = {}
waterToFlow[boundsLow[0],boundsLow[1],boundsLow[2]] = 1
done = False
while not done:
    newwater = {}
    done = True
    length = 0
    for i in waterToFlow:
        for j in check:
            toadd = (i[0]+j[0],i[1]+j[1],i[2]+j[2])
            if toadd not in water and toadd[0]>=boundsLow[0] and toadd[1]>=boundsLow[1] and toadd[2]>=boundsLow[2] and toadd[0]<=boundsHigh[0] and toadd[1]<=boundsHigh[1] and toadd[2]<=boundsHigh[2]:
                if toadd in grid:
                    area += 1
                else:
                    length += 1
                    newwater[toadd] = 1
                    done = False
    waterToFlow = {}
    for i in newwater:
        water[i] = 1
        waterToFlow[i] = 1
print(area)