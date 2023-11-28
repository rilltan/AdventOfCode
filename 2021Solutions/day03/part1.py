import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

g = ""
e = ""
for i in range(len(data[0])):
    if [num[i] for num in data].count("1") >= len(data)/2:
        g+="1"
        e+="0"
    else:
        g+="0"
        e+="1"

print(int(g,2)*int(e,2))