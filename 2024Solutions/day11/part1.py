import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def evolve(stones):
    new = []
    for i in range(len(stones)):
        l = len(str(stones[i]))
        if stones[i]==0:
            new.append(1)
        elif l%2==0:
            new.append(int(str(stones[i])[:l//2]))
            new.append(int(str(stones[i])[(l//2):]))
        else:
            new.append(stones[i]*2024)
    return new

a = getints(data[0])
for i in range(25):
    a = evolve(a)
prco(len(a))