import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

result = 0
for x in data[0]:
    result += {"(":1,")":-1}[x]

prco(result)