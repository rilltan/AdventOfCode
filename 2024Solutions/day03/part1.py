import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def mul(x,y):
    return x*y

lines = "".join(data)
muls = re.findall(r'mul\(\d+,\d+\)',lines)

prco(sum(eval(x) for x in muls))