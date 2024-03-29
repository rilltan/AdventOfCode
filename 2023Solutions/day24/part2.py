import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [getints(x) for x in data]

def findline(a,b,h1,h2):
    # a,b,c = velocity of rock
    # x,y,z = starting position of rock
    # h1/h2 = coefficients of vector equation for first/second hailstone
    # t1/t2 = time when first/second hailstone collides with rock

    # Given a, b, h1, and h2, we want to find x,y,z,c such that:
    # [x,y,z] + t1*[a,b,c] = [h1.x,h1.y,h1.z] + t1*[h1.a,h1.b,h1.c]
    # [x,y,z] + t2*[a,b,c] = [h2.x,h2.y,h2.z] + t2*[h2.a,h2.b,h2.c]
    # ( [1,2,3] represents a vector )
    
    # After some maths these simultaneous equations become
    # [x] = [k1  -1]^-1 * [k1*h1.x-h1.y]
    # [y] = [k2  -1]      [k2*h2.x-h1.y]
    # where k1 = (h1.b-b) / (h1.a-a) and k2 = (h2.b-b) / (h2.a-a)
    # Solving for x and y:
    if h1[3] == a or h2[3]==a:
        return False
    k1 = (h1[4]-b)/(h1[3]-a)
    k2 = (h2[4]-b)/(h2[3]-a)
    det = k2 - k1
    if det==0:
        return False
    x = round((k2*h2[0] - h2[1] - k1*h1[0] + h1[1]) / det)
    y = round((k1*(k2*h2[0]-h2[1]) - k2*(k1*h1[0]-h1[1])) / det)

    # x + t1*c = h1.x + t2*h1.x
    # x + t2*c = h2.x + t2*h2.x
    # Solving for t1 and t2
    time1 = (x-h1[0])//(h1[3]-a)
    time2 = (x-h2[0])//(h2[3]-a)

    # z + t*c = h1.z + t*h1.c
    # z + t*c = h2.z + t*h2.c
    # Solving for z and c
    det = time1 - time2
    m1 = h1[2] + h1[5]*time1
    m2 = h2[2] + h2[5]*time2
    c = (m1 - m2) // det
    z = (time1*m2 - time2*m1) // det
    
    return (x,y,z,c)

def intersect(h1,h2):
    times = []
    # Get the times when the rocks/hailstones have the same x, y, or z value
    for i in range(3):
        try:
            times.append((h1[i]-h2[i])/(h2[i+3]-h1[i+3]))
        except ZeroDivisionError:
            pass
    # Check if the times for x, y, and z intersections are all the same
    if times[0]>0 and all(times[i]==times[i+1] for i in range(len(times)-1)):
        return True
    return False

# I increased the search range until I got an answer
r1 = -200
r2 = 200
def solve():
    for a in incrange(r1,r2):
        for b in incrange(r1,r2):
            linedata = findline(a,b,data[0],data[1])
            if linedata:
                x,y,z,c = linedata
                if all(intersect((x,y,z,a,b,c),h) for h in data):
                    return x+y+z
    return 0

print(solve())