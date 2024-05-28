import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

result = 0

for line in data:
    l,w,h = getints(line)
    result += 2*(l*w+l*h+h*w) + min(l*w,l*h,h*w)

prco(result)