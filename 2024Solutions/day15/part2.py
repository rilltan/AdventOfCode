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
            boxes.add((x*2,y))
        elif data[y][x] == "#":
            walls.add((x*2,y))
            walls.add((x*2+1,y))
        elif data[y][x] == "@":
            bot = (x*2,y)

# this code is an absolute mess but it works, I might improve it later
dirs = "".join(data[data.index("")+1:])
xsize = len(data[0])
ysize = data.index("")
dirsV = {"^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}
for c in dirs:
    if (bot[0]+dirsV[c][0],bot[1]+dirsV[c][1]) in walls:
        continue
    i = 1
    connected = []
    end = []
    if c =="^" or c=="v":
        if (bot[0],bot[1]+dirsV[c][1]) in boxes:
            connected.append((bot[0],bot[1]+dirsV[c][1]))
            end.append((bot[0],bot[1]+dirsV[c][1]))
        elif (bot[0]-1,bot[1]+dirsV[c][1]) in boxes:
            connected.append((bot[0]-1,bot[1]+dirsV[c][1]))
            end.append((bot[0]-1,bot[1]+dirsV[c][1]))
        while not all([(a[0],a[1]+dirsV[c][1]) not in boxes and (a[0]+1,a[1]+dirsV[c][1]) not in boxes and( a[0]-1,a[1]+dirsV[c][1]) not in boxes for a in end]):
            endtemp = [a for a in end]
            for box in endtemp:
                if (box[0],box[1]+dirsV[c][1]) in boxes:
                    if (box[0],box[1]+dirsV[c][1]) not in connected:
                        connected.append((box[0],box[1]+dirsV[c][1]))
                        end.append((box[0],box[1]+dirsV[c][1]))
                    end.remove(box)
                if (box[0]+1,box[1]+dirsV[c][1]) in boxes:
                    if (box[0]+1,box[1]+dirsV[c][1]) not in connected:
                        connected.append((box[0]+1,box[1]+dirsV[c][1]))
                        end.append((box[0]+1,box[1]+dirsV[c][1]))
                    end.remove(box)
                if (box[0]-1,box[1]+dirsV[c][1]) in boxes:
                    if (box[0]-1,box[1]+dirsV[c][1]) not in connected:
                        connected.append((box[0]-1,box[1]+dirsV[c][1]))
                        end.append((box[0]-1,box[1]+dirsV[c][1]))
                    if box in end:
                        end.remove(box)
        if any([(a[0],a[1]+dirsV[c][1]) in walls or (a[0]+1,a[1]+dirsV[c][1]) in walls for a in connected]):
            continue
        for box in connected[::-1]:
            boxes.remove(box)
            boxes.add((box[0],box[1]+dirsV[c][1]))
        bot = (bot[0]+dirsV[c][0],bot[1]+dirsV[c][1])
    else:
        if (bot[0]+dirsV[c][0],bot[1]) in boxes:
            connected.append((bot[0]+dirsV[c][0],bot[1]))
            end.append((bot[0]+dirsV[c][0],bot[1]))
        elif (bot[0]+dirsV[c][0]-1,bot[1]) in boxes:
            connected.append((bot[0]+dirsV[c][0]-1,bot[1]))
            end.append((bot[0]+dirsV[c][0]-1,bot[1]))
        while end and (end[-1][0]+dirsV[c][0]*2,end[-1][1]) in boxes:
            end.append((end[-1][0]+dirsV[c][0]*2,end[-1][1]))
            end.remove((end[-2][0],end[-2][1]))
            connected.append((end[-1][0],end[-1][1]))
        if end and ((end[-1][0]+dirsV[c][0],end[-1][1]) in walls or (end[-1][0]+2,end[-1][1]) in walls):
            continue
        for box in connected:
            boxes.remove(box)
            boxes.add((box[0]+dirsV[c][0],box[1]))
        bot = (bot[0]+dirsV[c][0],bot[1]+dirsV[c][1])

prco(sum(a[1]*100+a[0] for a in boxes   ))