import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [getints(x) for x in data]
result = 0
for line in data:
    result += int(str(line[0])[0])*10 + int(str(line[-1])[-1])

prco(result)