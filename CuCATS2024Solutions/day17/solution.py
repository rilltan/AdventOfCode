import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

nums = getints(data[1])
each = sum(nums)//len(nums)
count = 0
while any(x != each for x in nums):
    count += 1
    toadd = [0 for _ in nums]
    for i,n in enumerate(nums):
        if n > 0:
            if sum(nums[:i]) < each*(i):
                toadd[i-1] += 1
                toadd[i] -= 1
            elif sum(nums[i+1:]) < each*(len(nums)-i-1):
                toadd[i+1] += 1
                toadd[i] -= 1
    for i in range(len(nums)):
        nums[i] += toadd[i]

prco(count)