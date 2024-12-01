import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

lines = [x for x in data[1:]]

x,y = getints(lines[-1])
bestx,besty = 0,0
for line in lines:
    a,b = getints(line)
    if ((a-x)**2 + (b-y)**2 > ((bestx-x)**2  + (besty-y)**2 )):
        bestx,besty = a,b

prco((bestx-x,besty-y))