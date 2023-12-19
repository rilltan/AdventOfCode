import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = splitlist(data,"")[0]

maps = {}
for j,line in enumerate(data):
    name = line.split("{")
    maps[name[0]] = []
    stuff = name[1].split(",")
    for i in range(len(stuff)-1):
        ways = stuff[i].split(":")
        maps[name[0]].append((ways[0],ways[1]))
    maps[name[0]].append(("x>0",stuff[-1][:-1]))

def explore(func,ranges):
    ways = 0
    for rule in maps[func]:
        letter = rule[0][0]
        num = int(rule[0][2:])
        original = ranges[letter]

        ranges[letter] = (max(original[0],num+1),original[1]) if rule[0][1] == ">" else (original[0],min(original[1],num-1))
        if rule[1] == "A":
            ways += product(ranges[x][1]-ranges[x][0]+1 for x in ranges)
        elif rule[1] != "R":
            oldranges = {a:b for a,b in ranges.items()}
            ways += explore(rule[1],ranges)
            ranges = {a:b for a,b in oldranges.items()}
        
        ranges[letter] = (max(original[0],num),original[1]) if rule[0][1] == "<" else (original[0],min(original[1],num))
    return ways

prco(explore("in",{"x":(1,4000),"m":(1,4000),"a":(1,4000),"s":(1,4000)}))