import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

heights = makegrid(len(data),len(data[0]),-1)
for r in range(len(data)):
    for c in range(len(data[0])):
        heights[r][c] = int(data[r][c])

cardinals = u_cardinals
lows = []
for r in range(len(data)):
    for c in range(len(data[0])):
        low = True
        for ra,ca in cardinals:
            if ra+r >= 0 and ca+c >= 0 and ra+r < len(data) and ca+c < len(data[0]):
                if heights[r][c] >= heights[ra+r][ca+c]:
                    low = False
        if low:
            lows.append((r,c))

largestsizes = [0,0,0]
for r,c in lows:
    prevsize = -1
    visited = {(r,c)}
    while prevsize != len(visited):
        prevsize = len(visited)
        new = set()
        for ra,ca in visited:
            for rb,cb in cardinals:
                if ra+rb >= 0 and ca+cb >= 0 and ra+rb < len(data) and ca+cb < len(data[0]):
                    if heights[ra+rb][ca+cb] > heights[r][c] and heights[ra+rb][ca+cb] != 9:
                        new.add((ra+rb,ca+cb))
        visited.update(new)
    if len(visited) > largestsizes[0]:
        largestsizes[0] = len(visited)
        largestsizes = sorted(largestsizes)

print(product(largestsizes))