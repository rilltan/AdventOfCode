import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

positions = set([(0,0)])
pos1 = (0,0)
pos2 = (0,0)
for i,x in enumerate(data[0]):
    if i%2 == 0:
        pos1 = (pos1[0]+u_dirsV[x][0],pos1[1]+u_dirsV[x][1])
        positions.add(pos1)
    else:
        pos2 = (pos2[0]+u_dirsV[x][0],pos2[1]+u_dirsV[x][1])
        positions.add(pos2)
prco(len(positions))