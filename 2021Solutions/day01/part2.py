import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinputints(os.path.join(os.path.dirname(__file__),"input.txt"))

r = 0
for i in range(4,len(data)):
    if data[i]+data[i-1]+data[i-2] > data[i-1]+data[i-2]+data[i-3]:
        r+=1

print(r)