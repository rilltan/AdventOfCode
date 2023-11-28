import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinputints(os.path.join(os.path.dirname(__file__),"input.txt"))

print(len([i for i in range(1,len(data)) if data[i]>data[i-1]]))
print(len([i for i in range(4,len(data)) if data[i]+data[i-1]+data[i-2]>data[i-1]+data[i-2]+data[i-3] and i!=0]))