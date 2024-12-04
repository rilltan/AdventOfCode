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
for i in range(len(data)):
    for j in range(len(data[0])):
        if (i,j) in m and (i,j+2) in m and (i+2,j) in s and (i+2,j+2) in s and (i+1,j+1) in a:
            r += 1
        if (i,j) in m and (i,j+2) in s and (i+2,j) in m and (i+2,j+2) in s and (i+1,j+1) in a:
            r += 1
        if (i,j) in s and (i,j+2) in s and (i+2,j) in m and (i+2,j+2) in m and (i+1,j+1) in a:
            r += 1
        if (i,j) in s and (i,j+2) in m and (i+2,j) in s and (i+2,j+2) in m and (i+1,j+1) in a:
            r += 1
        
prco(r)