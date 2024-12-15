import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

boxes = set()
bot = (-1,-1)
walls = set()
for y in range(data.index("")):
    for x in range(len(data[0])):
        if data[y][x] == "O":
            boxes.add((x,y))
        elif data[y][x] == "#":
            walls.add((x,y))
        elif data[y][x] == "@":
            bot = (x,y)
dirs = "".join(data[data.index("")+1:])
xsize = len(data[0])
ysize = data.index("")
dirsV = {"^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}


for c in dirs:
    i = 1
    while (bot[0]+i*dirsV[c][0],bot[1]+i*dirsV[c][1]) in boxes:
        i += 1
    if (bot[0]+i*dirsV[c][0],bot[1]+i*dirsV[c][1]) in walls:
        continue
    
    if i != 1:
        boxes.remove((bot[0]+dirsV[c][0],bot[1]+dirsV[c][1]))
        boxes.add((bot[0]+i*dirsV[c][0],bot[1]+i*dirsV[c][1]))
    bot = (bot[0]+dirsV[c][0],bot[1]+dirsV[c][1])

for y in range(data.index("")):
    for x in range(len(data[0])):
        if (x,y) in boxes:
            print("O",end="")
        else:
            print(".",end="")
    print()

prco(sum(a[1]*100+a[0] for a in boxes   ))