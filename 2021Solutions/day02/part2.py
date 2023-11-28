import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x = 0
y = 0
aim = 0
for a in data:
    b = a.split(" ")
    if b[0] == "forward":
        x += int(b[1])
        y += int(b[1]) * aim
    elif b[0] == "up":
        aim -= int(b[1])
    else:
        aim += int(b[1])

print(x*y)