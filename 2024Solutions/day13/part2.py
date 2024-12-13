import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
import numpy

def tokens(ax,ay,bx,by,tx,ty):
    # these equations come from (ax,bx)(i) = (tx)
    #                           (ay,by)(j)   (ty)
    # which is solved by multiplying the inverse of the first matrix with the second
    i = (by*tx-bx*ty)//(ax*by-ay*bx)
    j = (-ay*tx+ax*ty)//(ax*by-ay*bx)
    if i*ax+j*bx != tx or i*ay+j*by != ty:
        return 0
    return i*3+j

r=0
for i,line in  enumerate(data):
    if i%4==0:
        a = getints(line)
    elif i%4==1:
        b = getints(line)
    elif i%4==2:
        t =  getints(line)
        r += tokens(a[0],a[1],b[0],b[1],t[0]+10000000000000,t[1]+10000000000000)

prco(r)