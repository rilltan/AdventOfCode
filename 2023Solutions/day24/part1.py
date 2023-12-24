import os
import sys
import itertools
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [getints(x) for x in data]

def intersect(h1,h2,bound1,bound2):
    # h1 = coefficients of vector equation for first hailstone
    # h2 = coefficients of vector equation for second hailstone
    
    # Getting h1 and h2 in the form ax + by + c = 0
    # a = 1 so we can ignore it
    b1 = -(h1[4]/h1[3])
    c1 = h1[0]*(h1[4]/h1[3])-h1[1]
    b2 = -(h2[4]/h2[3])
    c2 = h2[0]*(h2[4]/h2[3])-h2[1]

    # Solving for x and y (intersection point)
    # [a1 b1]^-1 * [c1] = [x]
    # [a2 b2]      [c2]   [y]
    det = b2 - b1
    if det == 0:
        return False
    x = (c1 - c2) / det
    y = (b1*c2 - b2*c1) / det

    # Solving for t (time each hailstone reaches intersection)
    # f(t) = start x + vel x * t
    time1 = (x-h1[0]) / h1[3]
    time2 = (x-h2[0]) / h2[3]
    if time1 > 0 and time2 > 0:
        if inbounds(x,bound1,bound2) and inbounds(y,bound1,bound2):
            return True
    return False

result = 0
for h1,h2 in itertools.combinations(data,2):
    if intersect(h1,h2,200000000000000,400000000000000):
        result += 1

print(result)