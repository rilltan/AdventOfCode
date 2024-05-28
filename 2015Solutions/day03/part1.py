import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

positions = set([(0,0)])
pos = (0,0)
for x in data[0]:
    pos = (pos[0]+u_dirsV[x][0],pos[1]+u_dirsV[x][1])
    positions.add(pos)
prco(len(positions))