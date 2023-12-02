import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [x.split(" ")[2:] for x in data]
result = 0
for i,x in enumerate(data):
    good = True
    for j in range(len(x)//2):
        if int(x[j*2]) > 12 and re.match("red",x[j*2+1]):
            good = False
        if int(x[j*2]) > 13 and re.match("green",x[j*2+1]):
            good = False
        if int(x[j*2]) > 14 and re.match("blue",x[j*2+1]):
            good = False
    if good:
        result += i+1

prco(result)