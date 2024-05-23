import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x1,x2,y1,y2 = getints(data[0])

minX_v = math.ceil(-0.5 + math.sqrt(0.25+2*x1))
maxX_v = x2

possibleY_v = []
for y_v in incrange(y1,-y1):
    enterTime = math.ceil(y_v + 0.5 + math.sqrt(y_v*y_v + y_v + 0.25 - 2*y2))
    exitTime = math.ceil(y_v + 0.5 + math.sqrt(y_v*y_v + y_v + 0.25 - 2*(y1-1))) - 1
    if exitTime >= enterTime:
        if possibleY_v and possibleY_v[-1][1] == y_v - 1:
            possibleY_v[-1] = (possibleY_v[-1][0],y_v)
        else:
            possibleY_v.append((y_v,y_v))

total = 0
for x_v in incrange(minX_v,maxX_v):
    enterTime = math.ceil(x_v + 0.5 - math.sqrt(x_v*x_v + x_v + 0.25 - 2*x1))
    if (x_v*(x_v+1))//2 <= x2:
        exitTime = 9999999
    else:
        exitTime = math.ceil(x_v + 0.5 - math.sqrt(x_v*x_v + x_v + 0.25 - 2*(x2+1))) - 1
    if exitTime >= enterTime:
        minyvel = math.ceil(enterTime/2 + y1/enterTime - 0.5)
        maxyvel = math.floor(exitTime/2 + y2/exitTime - 0.5)
        for yrange in possibleY_v:
            total += max(0, min(yrange[1],maxyvel) - max(yrange[0],minyvel) + 1)

prco(total)