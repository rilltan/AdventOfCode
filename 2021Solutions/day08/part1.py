import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [x.split(" ") for x in data]
sum = 0
for i in data:
    for j in range(11,15):
        if len(i[j]) in {2,4,3,7}:
            sum += 1
print(sum)