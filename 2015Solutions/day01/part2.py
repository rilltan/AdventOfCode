import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

result = 0
pos = -1
for i,x in enumerate(data[0]):
    result += {"(":1,")":-1}[x]
    if result == -1:
        pos = i + 1
        break

prco(i)