import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

ps = []
vs = []
for line in data:
    nums = getints(line)
    ps.append((nums[0],nums[1]))
    vs.append((nums[2],nums[3]))

flag = True
secs = 0
while flag:
    secs += 1
    b = set()
    for i in range(len(ps)):
        ps[i] = ((ps[i][0]+vs[i][0])%101,(ps[i][1]+vs[i][1])%103)
        b.add(ps[i])
    if len(b) == len(ps):
        flag = False

for y in range(103):
    for x in range(101):
        if (x,y) in b:
            print("#",end="")
        else:
            print(" ",end="")
    print()
prco(secs)
