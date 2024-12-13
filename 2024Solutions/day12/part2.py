import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

def find_region(x,y):
    seen = set()
    letter = data[y][x]
    current = (x,y)
    next = deque()
    next.append((x,y))
    seen.add((x,y))
    while next:
        current = next.popleft()
        for dx,dy in u_cardinals:
            if (current[0]+dx,current[1]+dy) not in seen and inbounds(current[0]+dx,0,len(data[0])-1) and inbounds(current[1]+dy,0,len(data)-1):
                if data[current[1]+dy][current[0]+dx] == letter:
                    next.append((current[0]+dx,current[1]+dy))
                    seen.add((current[0]+dx,current[1]+dy))
    return seen

def num_sides(region):
    sides = set()
    for loc in region:
        for dx,dy in u_cardinals:
            if (loc[0]+dx,loc[1]+dy) not in region:
                sides.add((loc[0]*10+dx,loc[1]*10+dy))
    out = 0
    while sides:
        current = sides.pop()
        out += 1
        if current[0]%10==0:
            i = 1
            while (current[0]+i*10,current[1]) in sides:
                sides.remove((current[0]+i*10,current[1]))
                i+=1
            i = -1
            while (current[0]+i*10,current[1]) in sides:
                sides.remove((current[0]+i*10,current[1]))
                i-=1
        else:
            i = 1
            while (current[0],i*10+current[1]) in sides:
                sides.remove((current[0],i*10+current[1]))
                i+=1
            i = -1
            while (current[0],i*10+current[1]) in sides:
                sides.remove((current[0],i*10+current[1]))
                i-=1
    return out

all = set()
for x in range(len(data[0])):
    for y in range(len(data)):
        all.add((x,y))

regions = []
while all:
    loc = all.pop()
    regions.append(find_region(loc[0],loc[1]))
    all = all.difference(regions[-1])


prco(sum(len(x)*num_sides(x) for x in regions))