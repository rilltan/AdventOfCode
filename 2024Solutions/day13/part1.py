import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def tokens(ax,ay,bx,by,tx,ty):
    best = (-1,-1)
    for i in range(100):
        if (tx-ax*i)%bx == 0 and (ty-ay*i)%by == 0:
            if (tx-ax*i)//bx == (ty-ay*i)//by:
                bpresses = (tx-ax*i)//bx
                if best == (-1,-1) or (best[0] != -1 and bpresses + 3 * i < 3*best[0]+best[1]):
                    best = (i,bpresses)
    if best == (-1,-1):
        return 0
    return best[1] + 3 * best[0]

r=0
for i,line in  enumerate(data):
    if i%4==0:
        a = getints(line)
    elif i%4==1:
        b = getints(line)
    elif i%4==2:
        t =  getints(line)
        r += tokens(a[0],a[1],b[0],b[1],t[0],t[1])
prco(r)