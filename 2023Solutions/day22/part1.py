import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [getints(x) for x in data]

def iterbrick(brick):
    return ((x,y,z) for z in incrange(brick[0][2],brick[1][2]) for y in incrange(brick[0][1],brick[1][1]) for x in incrange(brick[0][0],brick[1][0]))

bricks = [[[x[0],x[1],x[2]],[x[3],x[4],x[5]]] for x in data]
bricks.sort(key=lambda x:min(x[0][2],x[1][2]))

maxx = max(max(x[0][0],x[1][0]) for x in bricks)
maxy = max(max(x[0][1],x[1][1]) for x in bricks)
maxz = max(max(x[0][2],x[1][2]) for x in bricks)
grid = [makegrid(maxy+1,maxz+1,-1) for _ in range(maxx+1)] 
for i in range(len(bricks)):
    for x,y,z in iterbrick(bricks[i]):
        grid[x][y][z] = i

settled = [False for _ in bricks]

while any(not x for x in settled):
    for i in range(len(bricks)):
        if settled[i]:
            continue
        if bricks[i][0][2] == 1:
            settled[i] = True
            continue

        fall = True
        for x,y,z in iterbrick(bricks[i]):
            if grid[x][y][z-1] != -1 and z-1<bricks[i][0][2]:
                fall = False
        if fall:
            bricks[i][0][2] -= 1
            bricks[i][1][2] -= 1
            for x,y,z in iterbrick(bricks[i]):
                grid[x][y][z+1] = -1
                grid[x][y][z] = i
        else:
            settled[i] = True

supporting = [set() for i in range(len(bricks))]
supportedby = [set() for i in range(len(bricks))]

for i in range(len(bricks)):
    for (x,y,z) in iterbrick(bricks[i]):
        above = -1
        if z+1 <= maxz:
            above = grid[x][y][z+1]
        if above != -1 and above != i:
            supporting[i].add(above)
            supportedby[above].add(i)

result = 0
for i in range(len(bricks)):
    candisintegrate = 1
    for j in supporting[i]:
        if len(supportedby[j])<=1:
            candisintegrate = 0
    result += candisintegrate

prco(result)