import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

wires = {}
for line in data:
    gate,output = line.split(" -> ")
    gate = gate.split()
    wires[output] = gate

def signal(x):
    if x.isdigit():
        return int(x)
    if type(wires[x]) is int:
        return wires[x]
     
    if len(wires[x]) == 1:
        wires[x] = signal(wires[x][0])
    elif len(wires[x]) == 2:
        wires[x] = ~signal(wires[x][1]) & 65535
    elif wires[x][1] == "OR":
        wires[x] = signal(wires[x][0]) | signal(wires[x][2])
    elif wires[x][1] == "AND":
        wires[x] = signal(wires[x][0]) & signal(wires[x][2])
    elif wires[x][1] == "LSHIFT":
        wires[x] = signal(wires[x][0]) << int(wires[x][2])
    elif wires[x][1] == "RSHIFT":
        wires[x] = signal(wires[x][0]) >> int(wires[x][2])
    
    return wires[x]

prco(signal("a"))