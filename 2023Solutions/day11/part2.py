import os
import sys
import itertools as it
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

emptyr = []
emptyc = []

for i,line in enumerate(data):
    if "#" not in line:
        emptyr.append(i)
for i,column in enumerate([[line[k] for line in data] for k in range(len(data))]):
    if "#" not in column:
        emptyc.append(i)

points = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "#":
            points.append((r,c))

result = 0
for p1,p2 in it.combinations(points,2):
    result += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    for r in emptyr:
        if inbounds(r,p1[0],p2[0]):
            result += 999999
    for c in emptyc:
        if inbounds(c,p1[1],p2[1]):
            result += 999999

prco(result)