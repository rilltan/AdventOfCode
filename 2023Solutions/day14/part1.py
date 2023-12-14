import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

result = 0
for column in [[x[a] for x in data] for a in range(len(data))]:
    i = 0
    for j in range(len(column)):
        if column[j] == "O":
            result += len(column)-i
            i+=1
        elif column[j] == "#":
            i = j+1
prco(result)