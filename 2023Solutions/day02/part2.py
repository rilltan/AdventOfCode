import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [x.split(" ")[2:] for x in data]
result = 0
for i,x in enumerate(data):
    red = 0
    blue = 0
    green = 0
    for j in range(len(x)//2):
        if int(x[j*2]) > red and re.match("red",x[j*2+1]):
            red = int(x[j*2])
        if int(x[j*2]) > green and re.match("green",x[j*2+1]):
            green = int(x[j*2])
        if int(x[j*2]) > blue and re.match("blue",x[j*2+1]):
            blue = int(x[j*2])
    result += red*green*blue

prco(result)