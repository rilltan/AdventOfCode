import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = splitlist(data,"")

maps = {}
for j,line in enumerate(data[0]):
    name = line.split("{")
    maps[name[0]] = []
    rules = name[1].split(",")
    for i in range(len(rules)-1):
        x = rules[i].split(":")
        maps[name[0]].append((x[0],x[1]))
    maps[name[0]].append(("True",rules[-1][:-1]))

def sim(x,m,a,s,func):
    for line in maps[func]:
        if eval(line[0]):
            if line[1] == "A":
                return True
            if line[1] == "R":
                return False
            return sim(x,m,a,s,line[1])

result = 0
for i,line in enumerate(data[1]):
    x,m,a,s = 0,0,0,0
    for command in removechars(line,"{}").split(","):
        exec(command)
    if sim(x,m,a,s,"in"):
        result += x+m+a+s

prco(result)