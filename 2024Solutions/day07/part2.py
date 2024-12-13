import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
import functools

def oom(n):
    if n<10:
        return 10
    if n<100:
        return 100
    if n<1000:
        return 1000
    if n<10000:
        return 10000
    if n<100000:
        return 100000
    if n<1000000:
        return 1000000
    if n<10000000:
        return 10000000
    if n<100000000:
        return 100000000
    if n<1000000000:
        return 1000000000
    if n<10000000000:
        return 10000000000
    if n<100000000000:
        return 100000000000
    if n<1000000000000:
        return 1000000000000
    if n<10000000000000:
        return 10000000000000
    if n<100000000000000:
        return 100000000000000
    if n<1000000000000000:
        return 1000000000000000
    raise Exception

def ans(final, nums):
    if final < 0:
        return False
    if not nums:
        return final == 0
    if ans(final-nums[-1],nums[:-1]):
        return True
    if final%nums[-1]==0 and final != 0:
        if ans(final//nums[-1],nums[:-1]):
            return True
    if oom(final)>oom(nums[-1]) and final%oom(nums[-1]) == nums[-1]:
        if ans(final//oom(nums[-1]),nums[:-1]):
            return True
    return False
        
r = 0
for line in data:
    nums = getints(line)
    if ans(nums[0],nums[1:]):
        r += nums[0]

prco(r)