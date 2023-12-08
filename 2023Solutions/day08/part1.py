import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

steps = data[0]
network = [re.findall(r"[A-Z]+",x) for x in data[2:]]
graph = {x:(y,z) for x,y,z in network}
dirs = {"R":1,"L":0}

i = 0
current = "AAA"
while current != "ZZZ":
    current = graph[current][dirs[steps[i%len(steps)]]]
    i += 1
prco(i)