import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [x.split()[2::] for x in data]
data = [splitlist(x, "|") for x in data]

result = 0
for line in data:
    matches = set(line[0]) & set(line[1])
    if matches:
        result += 2**(len(matches)-1)
        
prco(result)