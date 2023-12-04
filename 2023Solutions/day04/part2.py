import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [x.split()[2::] for x in data]
data = [splitlist(x, "|") for x in data]

copies = [1]*len(data)
for i,line in enumerate(data):
    matches = set(line[0]) & set(line[1])
    for j in range(len(matches)):
        copies[i+j+1] += copies[i]

prco(sum(copies))