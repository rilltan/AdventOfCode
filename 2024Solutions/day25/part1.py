import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

locks = []
keys = []
current = [0,0,0,0,0]
start = False
lock = False
for line in data:
    if line == "":
        if lock:
            locks.append(current.copy())
        else:
            keys.append(current.copy())
        current = [0,0,0,0,0]
        start = True
        continue
    if start:
        start = False
        if line == "#####":
            lock = True
        else:
            lock = False
    for i,c in enumerate(line):
        if c == "#":
            current[i] += 1

r=0
for key in keys:
    for lock in locks:
        if all(a+b <= 7 for a,b in zip(key,lock)):
            r+=1
print(r)