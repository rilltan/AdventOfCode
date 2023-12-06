import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

time = int("".join([str(x) for x in getints(data[0])]))
dist = int("".join([str(x) for x in getints(data[1])]))

ways = 0
for j in range(time):
    if j * (time-j) > dist:
        ways += 1

prco(ways)