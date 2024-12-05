import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def collide(nums):
    if len(nums)<=1:
        return nums
    new = []
    i = 0
    while i < len(nums)-1:
        if nums[i] > 0 and nums[i+1] < 0:
            if abs(nums[i]) > abs(nums[i+1]):
                new.append(nums[i])
            elif abs(nums[i]) < abs(nums[i+1]):
                new.append(nums[i+1])
            i += 2
        else:
            new.append(nums[i])
            i += 1
    if i == len(nums)-1:
        new.append(nums[-1])
    return new

def destroyed(nums):
    flag = False
    length = len(nums)
    while not flag:
        new = collide(nums)
        if len(new) == len(nums):
            flag = True
        nums = new
    return length-len(new)

prco(sum(destroyed(getints(x)) for x in data if len(getints(x))>1))