import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = splitlist(data,"")

result = 0
for grid in data:
    for c in range(1,len(grid[0])):
        errors = 0
        for r in grid:
            half1 = r[:c][::-1]
            half2 = r[c:]
            for letter1,letter2 in zip(half1,half2):
                if letter1 != letter2:
                    errors += 1
        if errors == 1:
            result += c
            break
    
    if errors != 1:
        for r in range(1,len(grid)):
            half1 = grid[:r][::-1]
            half2 = grid[r:]
            errors = 0
            for row1,row2 in zip(half1,half2):
                if row1!=row2:
                    for letter1,letter2 in zip(row1,row2):
                        if letter1!=letter2:
                            errors += 1
            if errors == 1:
                result += 100*r
                break

prco(result)