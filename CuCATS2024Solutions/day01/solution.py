import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x,y = getints(data[-1])
bestx,besty = 0,0
for line in data[1:]:
    a,b = getints(line)
    if ((a-x)**2 + (b-y)**2 > ((bestx-x)**2  + (besty-y)**2 )):
        bestx,besty = a,b

prco((bestx-x,besty-y))