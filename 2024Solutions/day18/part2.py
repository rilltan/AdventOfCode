import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
from collections import deque

def bfs(nums):
    c = (0,0)
    q = deque([c])
    lengths = {c:0}
    while c != (70,70):
        c = q.popleft()
        for d in u_cardinals:
            if (c[0]+d[0],c[1]+d[1]) not in lengths and (c[0]+d[0],c[1]+d[1]) not in nums and inbounds(c[0]+d[0],0,70) and inbounds(c[1]+d[1],0,70):
                q.append((c[0]+d[0],c[1]+d[1]))
                lengths[(c[0]+d[0],c[1]+d[1])] = lengths[c] + 1

nums = [(getints(x)[0],getints(x)[1]) for x in data]
lo = 0
hi = len(nums)
while True:
    a = False
    try:
        bfs(set(nums[:(lo+hi)//2]))
    except:
        a = True
    if a:
        hi = (lo+hi)//2
    else:
        lo = (lo+hi)//2 + 1
    if lo == hi:
        prco(nums[lo-1])
        break