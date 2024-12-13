import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
import functools

@functools.lru_cache(None)
def length(num,tries):
    if tries==0:
        return 1
    if num == 0:
        return length(1,tries-1)
    l = len(str(num))
    if l%2==0:
        return length(int(str(num)[:l//2]),tries-1) + length(int(str(num)[l//2:]),tries-1)
    return length(2024*num,tries-1)

prco(sum(length(x,75) for x in getints(data[0])))