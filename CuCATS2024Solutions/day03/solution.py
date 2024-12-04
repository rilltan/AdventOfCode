import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def ans(nums):
    out = 10000
    for j in range(3):
        if nums[0] == j:
            continue
        unique = [j]
        zaps = 0
        for i,n in enumerate(nums):
            if n in unique:
                unique.remove(n)
            if not unique:
                zaps += 1
                unique = [0,1,2]
                unique.remove(n)
                if nums[i-1] in unique:
                    unique.remove(nums[i-1])
        if j not in unique:
            zaps += 1
            if nums[-1] ==  j:
                zaps += 1
        
        if zaps < out:
            out = zaps
    return out

prco(sum(ans(getints(x)) for x in data[1:]))