import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x=set()
m=set()
a=set()
s=set()
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "X":
            x.add((i,j))
        if data[i][j] == "M":
            m.add((i,j))
        if data[i][j] == "A":
            a.add((i,j))
        if data[i][j] == "S":
            s.add((i,j))
r=0
for loc in x:
    for dir in u_adjacent:
        if (loc[0]+dir[0],loc[1]+dir[1]) in m and (loc[0]+2*dir[0],loc[1]+2*dir[1]) in a and (loc[0]+3*dir[0],loc[1]+3*dir[1]) in s:
            r+=1
prco(r)