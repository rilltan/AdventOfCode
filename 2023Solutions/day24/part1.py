import os
import sys
import numpy
import itertools
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [getints(x) for x in data]

def intersect(h1,h2,bound1,bound2):
    equ1 = (1,-(h1[4]/h1[3]),h1[0]*(h1[4]/h1[3])-h1[1])
    equ2 = (1,-(h2[4]/h2[3]),h2[0]*(h2[4]/h2[3])-h2[1])

    try:
        mat1 = numpy.linalg.inv([[equ1[0],equ1[1]],[equ2[0],equ2[1]]])
    except numpy.linalg.LinAlgError:
        return False
    mat2 = [[-equ1[2]],[-equ2[2]]]
    mat = numpy.matmul(mat1,mat2)

    x = mat[1][0]
    y = mat[0][0]
    time1 = (x-h1[0])/h1[3]
    time2 = (x-h2[0])/h2[3]
    if time1 > 0 and time2 > 0:
        if inbounds(x,bound1,bound2) and inbounds(y,bound1,bound2):
            return True
    return False

result = 0
for h1,h2 in itertools.combinations(data,2):
    if intersect(h1,h2,200000000000000,400000000000000):
        result += 1

prco(result)