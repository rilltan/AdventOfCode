import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [getints(x) for x in data]

# This is very unreadable, I simplified most of the maths and I don't really remember what each bit does
def findline(a,b,h1,h2):
    try:
        k1 = (h1[4]-b)/(h1[3]-a)
        k2 = (h2[4]-b)/(h2[3]-a)
    except ZeroDivisionError:
        return False
    
    det = k2 - k1
    if det==0:
        return False
    x = (k2*h2[0] - h2[1] - k1*h1[0] + h1[1]) / det
    y = (k1*(k2*h2[0]-h2[1]) - k2*(k1*h1[0]-h1[1])) / det

    time1 = round((x-h1[0])/(h1[3]-a))
    time2 = round((x-h2[0])/(h2[3]-a))
    
    det = time1 - time2
    m1 = h1[2] + h1[5]*time1
    m2 = h2[2] + h2[5]*time2
    c = (m1 - m2) / det
    z = (time1*m2 - time2*m1) / det
    return (round(i) for i in (x,y,z,c))

def intersect(h1,h2):
    times = []
    for i in range(3):
        try:
            times.append((h1[i]-h2[i])/(h2[i+3]-h1[i+3]))
        except ZeroDivisionError:
            pass
    if times[0]>0 and all(times[i]==times[i+1] for i in range(len(times)-1)):
        return True
    return False

r1 = -200
r2 = 200
def solve():
    for a in incrange(r1,r2):
        for b in incrange(r1,r2):
            linedata = findline(a,b,data[0],data[1])
            if linedata:
                good = True
                x,y,z,c = linedata
                for h in data:
                    if not intersect((x,y,z,a,b,c),h):
                        good = False
                        break
                if good:
                    return x+y+z
    return 0

prco(solve())