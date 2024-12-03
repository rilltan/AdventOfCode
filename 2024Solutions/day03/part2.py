import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def mul(x,y):
    return x*y

lines = "".join(data)
muls=re.finditer(r'mul\(\d+,\d+\)',lines)

r=0
for m in muls:
    do = lines.rfind("do()",0,m.span()[0])
    dont = lines.rfind("don't()",0,m.span()[0])
    if do >= dont:
        r += eval(m.group())

prco(r)