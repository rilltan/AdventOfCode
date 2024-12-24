import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

states = {}
for i,line in enumerate(data):
    if line == "":
        wires = data[i+1:]
        break
    states[line[:3]] = 1 if line.split()[1] == "1" else 0

last = -1
zs = []
while len(states) != last:
    last = len(states)
    for line in wires:
        x = line.split()
        if x[0] in states and x[2] in states:
            if x[4][0] == "z" and x[4] not in zs:
                zs.append(x[4])
            if x[1] == "XOR":
                states[x[4]] = states[x[0]] ^ states[x[2]]
            if x[1] == "AND":
                states[x[4]] = states[x[0]] & states[x[2]]
            if x[1] == "OR":
                states[x[4]] = states[x[0]] | states[x[2]]

r = 0
for i,n in enumerate(sorted(zs)):
    r += (2**i) * states[n]
prco(r)