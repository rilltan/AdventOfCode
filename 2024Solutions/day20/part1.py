import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

points = set()
for y,ny in enumerate(data):
    for x,nx in enumerate(ny):
        if nx == ".":
            points.add((y,x))
        elif nx == "S":
            points.add((y,x))
            start = (y,x)
        elif nx == "E":
            points.add((y,x))
            end = (y,x)

times = {start: 0}
c = start
while c != end:
    for d in u_cardinals:
        if (c[0]+d[0],c[1]+d[1]) in points and (c[0]+d[0],c[1]+d[1]) not in times:
            times[(c[0]+d[0],c[1]+d[1])] = times[c] + 1
            c = (c[0]+d[0],c[1]+d[1])

out = 0
for p in points:
    for d in u_cardinals:
        q = (p[0]+d[0]*2,p[1]+d[1]*2)
        if q in points and times[q] - times[p] - 2 >= 100:
            out += 1

prco(out)