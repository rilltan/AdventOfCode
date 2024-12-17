import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
import functools


def canhalf(nums):
    # this uses this algorithm: https://en.wikipedia.org/wiki/Pseudopolynomial_time_number_partitioning
    if sum(nums)%2==1:
        return False
    p = makegrid(sum(nums)//2 + 1,len(nums)+1,False)
    for i in range(len(nums)+1):
        p[0][i] = True
    
    for i in range(1,sum(nums)//2+1):
        for j in range(1,len(nums)+1):
            element = nums[j-1]
            if i - element >= 0:
                p[i][j] = p[i][j-1] or p[i-element][j-1]
            else:
                p[i][j] = p[i][j-1]
    return p[sum(nums)//2][len(nums)]

@functools.lru_cache(None)
def canhalf2(target,elementindex,nums):
    if sum(nums)%2==1:
        return False
    
    if target == 0:
        return True
    if elementindex == 0:
        return False
    
    if target - nums[elementindex-1] >= 0:
        return canhalf2(target,elementindex-1,nums) or canhalf2(target - nums[elementindex-1], elementindex-1,nums)
    return canhalf2(target,elementindex-1,nums)


def ans(nums):
    nums = tuple(nums)
    if canhalf2(sum(nums)//2,len(nums),nums):
        return sum(nums)//2
    original = nums
    for i in range(1,len(nums)):
        for j in it.combinations(range(len(nums)),i):
            print(j)
            nums = original
            for k in j:
                nums = nums[:k] + nums[k+1:]
            if canhalf2(sum(nums)//2,len(nums),nums):
                return sum(nums)//2

nums = sorted(getints(data[1]))
prco(ans(nums))