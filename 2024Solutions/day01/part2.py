import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

l = []
r =  []
for line in data:
    a,b = getints(line)
    l.append(a)
    r.append(b)

x=0
for n in l:
    x += n * r.count(n)

prco(x)