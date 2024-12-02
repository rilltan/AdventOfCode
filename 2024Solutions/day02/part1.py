import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def safe(ns):
    good = True
    prev = ns[0]-ns[1] < 0
    for i in range(len(ns)-1):
        if abs(ns[i]-ns[i+1])>3:
            good = False
        if abs(ns[i]-ns[i+1])<1:
            good = False
        decrease = ns[i]-ns[i+1] < 0
        if decrease != prev:
            good = False
    return good

result = 0
for line in data:
    result += safe(getints(line))

prco(result)