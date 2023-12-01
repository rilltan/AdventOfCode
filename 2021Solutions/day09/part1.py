import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

heights = makegrid(len(data[0]),len(data),-1)
for r in range(len(data)):
    for c in range(len(data[0])):
        heights[r][c] = int(data[r][c])

result = 0
cardinals = u_cardinals
for r in range(len(data)):
    for c in range(len(data[0])):
        low = True
        for ra,ca in cardinals:
            if ra+r >= 0 and ca+c >= 0 and ra+r < len(data) and ca+c < len(data[0]):
                if heights[r][c] >= heights[ra+r][ca+c]:
                    low = False
        if low:
            result += 1 + heights[r][c]

print(result)