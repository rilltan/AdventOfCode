import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

import functools
@functools.lru_cache(None)
def score(s,clipboardUsed):
    if s == "":
        return 0
    best = 1 + score(s[:-1],clipboardUsed)
    for i in range(1,len(s)//2+1):
        end = s[-i:]
        if end in s[:-i]:
            best = min(best, (1 if clipboardUsed==s[-i:] else 2) + score(s[:-i],s[-i:]))
    return best

r = 0
for i,x in enumerate(data[1:]):
    r += score(x,"")
    if (i+1)%10 == 0:
        print(f"{i+1}% of lines completed")
prco(r)