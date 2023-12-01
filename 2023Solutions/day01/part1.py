import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [re.findall(r"\d",x) for x in data]
result = 0
for line in data:
    result += int(line[0]) * 10 + int(line[-1])

prco(result)