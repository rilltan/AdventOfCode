import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
import functools

@functools.lru_cache(None)
def ans(final, nums):
    if not nums:
        return final == 0
    if ans(final-nums[-1],nums[:-1]):
        return True
    if final%nums[-1]==0:
        if ans(final//nums[-1],nums[:-1]):
            return True


r = 0
for line in data:
    nums = tuple(getints(line))
    if ans(nums[0],nums[1:]):
        r += nums[0]
prco(r)