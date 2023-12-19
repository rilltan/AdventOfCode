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
    maps[name[0]].append(("True",stuff[-1][:-1]))

letters = ["x","m","a","s"]
def explore(func,ranges=[{"x":[],"m":[],"a":[],"s":[]}]):
    for line in maps[func]:
        if line[0] == "True":
            if line[1] == "A":
                ranges.append({"x":[x for x in ranges[-1]["x"]],"m":[x for x in ranges[-1]["m"]],"a":[x for x in ranges[-1]["a"]],"s":[x for x in ranges[-1]["s"]]})
                return ranges
            if line[1] == "R":
                return ranges
            return explore(line[1],ranges)
        if line[1] != "R":
            if line[0][1] == ">":
                ranges[-1][line[0][0]].append((int(line[0][2:])+1,4000))
            else:
                ranges[-1][line[0][0]].append((1,int(line[0][2:])-1))
            if line[1] == "A":
                ranges.append({"x":[x for x in ranges[-1]["x"]],"m":[x for x in ranges[-1]["m"]],"a":[x for x in ranges[-1]["a"]],"s":[x for x in ranges[-1]["s"]]})
                ranges[-1][line[0][0]][-1] = (int(line[0][2:]),4000) if line[0][1]=="<" else (1,int(line[0][2:]))
            else:
                lengths = [len(ranges[-1][x]) for x in letters]
                explore(line[1],ranges)
                for j,letter in enumerate(letters):
                    for i in range(-lengths[j]+len(ranges[-1][letter])):
                        ranges[-1][letter].pop()
                ranges[-1][line[0][0]][-1] = (int(line[0][2:]),4000) if line[0][1]=="<" else (1,int(line[0][2:]))

        else:
            if line[0][1] == "<":
                ranges[-1][line[0][0]].append((int(line[0][2:]),4000))
            else:
                ranges[-1][line[0][0]].append((1,int(line[0][2:])))

def combineranges(x,y):
    if x[1] < y[0] or x[0] > y[1]:
        return (0,-1)
    else:
        return (max(x[0],y[0]),min(x[1],y[1]))

result = 0
ranges = explore("in")
for lrange in ranges[:-1]:
    ways = 1
    for l in lrange:
        currentrange = (1,4000)
        for r in lrange[l]:
            currentrange = combineranges(currentrange,r)
        ways *= currentrange[1]-currentrange[0]+1
    result += ways
prco(result)