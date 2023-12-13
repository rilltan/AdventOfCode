import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = splitlist(data,"")

result = 0
for grid in data:
    for c in range(1,len(grid[0])):
        found = True
        for r in grid:
            half1 = r[:c][::-1]
            half2 = r[c:]
            length = min(len(half1),len(half2))
            if half1[:length] != half2[:length]:
                found = False
        if found:
            result += c
            break
    
    if not found:
        for r in range(1,len(grid)):
            found = True
            half1 = grid[:r][::-1]
            half2 = grid[r:]
            if any(row1 != row2 for row1,row2 in zip(half1,half2)):
                found = False
            if found:
                result += 100*r
                break

prco(result)