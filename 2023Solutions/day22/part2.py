import os
import sys
import copy
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [getints(x) for x in data]

def iterbrick(brick):
    return ((x,y,z) for z in incrange(brick[0][2],brick[1][2]) for y in incrange(brick[0][1],brick[1][1]) for x in incrange(brick[0][0],brick[1][0]))

bricks = [[[x[0],x[1],x[2]],[x[3],x[4],x[5]]] for x in data]
bricks = sorted(bricks,key=lambda x:min(x[0][2],x[1][2]))
brickset = set()
for brick in bricks:
    for x,y,z in iterbrick(brick):
        brickset.add((x,y,z))

settled = [False for _ in bricks]

while any(not x for x in settled):
    for i in range(len(bricks)):
        if settled[i]:
            continue
        if bricks[i][0][2] == 1:
            settled[i] = True
            continue

        brickfall = True
        for x,y,z in iterbrick(bricks[i]):
            if (x,y,z-1) in brickset and z-1<bricks[i][0][2]:
                brickfall = False
        if brickfall:
            bricks[i][0][2] -= 1
            bricks[i][1][2] -= 1
            for x,y,z in iterbrick(bricks[i]):
                brickset.remove((x,y,z+1))
                brickset.add((x,y,z))
        else:
            settled[i] = True

fall = 0
original = copy.deepcopy(brickset)
for brick in bricks:
    brickset = copy.deepcopy(original)
    zval = max(brick[0][2],brick[1][2])
    for x,y,z in iterbrick(brick):
        brickset.remove((x,y,z))
    
    for newbrick in bricks:
        if newbrick[0][2] == 1:
            continue
        brickfall = True
        for x,y,z in iterbrick(newbrick):
            if (x,y,z-1) in brickset and z-1<newbrick[0][2]:
                brickfall = False
        if brickfall:
            fall += 1
            for x,y,z in iterbrick(newbrick):
                brickset.remove((x,y,z))
                brickset.add((x,y,z-1))

prco(fall)

# This currently takes ~25s to run, I may improve it later