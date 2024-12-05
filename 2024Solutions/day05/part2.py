import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from functools import cmp_to_key

rules = set()
i=0
while data[i] != "":
    nums = getints(data[i])
    rules.add((nums[0],nums[1]))
    i+=1

def compare_nums(n1,n2):
    if (n1,n2) in rules:
        return -1
    else:
        return 1

i+=1
r = 0
while i < len(data):
    nums = getints(data[i])
    i+=1
    if not any((nums[j+1],nums[j]) in rules for j in range(len(nums)-1)):
        continue
    nums.sort(key=cmp_to_key(compare_nums))
    r += nums[len(nums)//2]

prco(r)