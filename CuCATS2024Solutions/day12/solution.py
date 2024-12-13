import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

heights = [(-999999999,999999999,0)]
r = 0
for flake in data[1:]:
    x,size = getints(flake)
    currentmax = 0
    for i,height in enumerate(heights):
        if currentmax < height[2] and x+size > height[0] and x < height[1]:
            currentmax = height[2]
    heights.append((x,x+size,currentmax+size))
    r += max(a[2] for a in heights)

prco(r)