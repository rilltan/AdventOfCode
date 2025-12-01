import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x = 50
r = 0
for line in data:
    x += int(line[1:]) * (-1 if line[0]=="L" else 1)
    x %= 100
    if x == 0:
        r += 1
        
prco(r)