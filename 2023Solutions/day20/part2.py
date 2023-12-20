import os
import sys
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

modules = {x.split(" -> ")[0][1:]:[y.strip() for y in x.split(" -> ")[1].split(",")] for x in data if x.split(" -> ")[0]!="broadcaster"} # {module name: module outputs}
modules["broadcaster"] = [[y.strip() for y in x.split(" -> ")[1].split(",")] for x in data if x.split(" -> ")[0]=="broadcaster"][0]
types = {x.split(" -> ")[0][1:]:x.split(" -> ")[0][0] for x in data if x.split(" -> ")[0]!="broadcaster"} # {module name: module type}
types["broadcaster"] = ""

flip = {x:0 for x in modules if types[x]=="%"}
conj = {x:{} for x in modules if types[x]=="&"}
for x in modules:
    for y in modules[x]:
        if y in types and types[y]=="&":
            conj[y][x] = 0

stack = deque()
for i in range(15000):
    stack.append((0,"broadcaster","")) # (value, destination, sender)
    while stack:
        val,dest,sender = stack.popleft()

        if dest == "vr" and val == 1:
            print(val,dest,sender,i)

        if dest == "output":
            continue
        if dest not in modules:
            continue

        if types[dest] == "":
            for x in modules["broadcaster"]:
                stack.append((val,x,"broadcaster"))
        elif types[dest] == "%":
            if val == 1:
                continue
            flip[dest] = (flip[dest]+1)%2
            for x in modules[dest]:
                stack.append((flip[dest],x,dest))
        elif types[dest] == "&":
            conj[dest][sender] = val
            val = int(any(x==0 for x in conj[dest].values()))
            for x in modules[dest]:
                stack.append((val,x,dest))

# In my puzzle input data, rx has one input, &vr, so for rx to recieve 0, vr must recieve all 1s
# When running this program, it outputs:
#   1 vr tn 3760
#   1 vr dr 3820
#   1 vr bm 3888
#   1 vr cl 3942
#   1 vr tn 7521
#   1 vr dr 7641
#   1 vr bm 7777
#   1 vr cl 7885
#   1 vr tn 11282
#   1 vr dr 11462
#   1 vr bm 11666
#   1 vr cl 11828
# vr's four inputs follow a linear sequence for when they output a 1
# I ran math.lcm(3760,3820,3888,3942) to get my answer