import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinputints(os.path.join(os.path.dirname(__file__),"input.txt"))

r = 0
prev = 1000000000
for i in data:
    if i > prev:
        r+=1
    prev = i
    
print(r)