import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = getints(data[0])

for i in range(80):
    length = len(data)
    for j in range(length):
        data[j]-=1
        if data[j] == -1:
            data.append(8)
            data[j] = 6
print(len(data))