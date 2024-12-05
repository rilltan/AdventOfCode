import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

rules = set()
i=0
while data[i] != "":
    nums = getints(data[i])
    rules.add((nums[0],nums[1]))
    i+=1

r = 0
i+=1
while i < len(data):
    nums = getints(data[i])
    i+=1
    if any((nums[j+1],nums[j]) in rules for j in range(len(nums)-1)):
        continue
    r += nums[len(nums)//2]

prco(r)