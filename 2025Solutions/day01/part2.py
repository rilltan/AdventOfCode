import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x = 50
r = 0
for line in data:
    a = x == 0
    x += int(line[1:]) * (-1 if line[0]=="L" else 1)

    if x >= 100:
        r += abs(x)//100
    elif x <= 0:
        r += abs(x)//100 + 1 - a

    x %= 100

prco(r)