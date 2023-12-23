import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

dirs = {"<":(0,-1),">":(0,1),"v":(1,0),"^":(-1,0)}

sys.setrecursionlimit(3000)

def dfs(r,c,seen:set,longest):
    seen.add((r,c))
    if r==len(data)-1:
        seen.remove((r,c))
        return len(seen)
    if data[r][c] !="." and data[r][c]!="#":
        ra = dirs[data[r][c]][0]
        ca = dirs[data[r][c]][1]
        if (ra+r,ca+c) not in seen:
            longest = max(longest, dfs(r+ra,c+ca,seen,longest))
    else:
        for ra,ca in u_cardinals:
            if data[ra+r][c+ca] != "#" and (ra+r,ca+c) not in seen:
                longest = max(longest, dfs(r+ra,c+ca,seen,longest))
    seen.remove((r,c))
    return longest

prco(dfs(0,1,set(),0))