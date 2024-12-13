import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

freq = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != ".":
            if data[i][j] not in freq:
                freq[data[i][j]] = []
            freq[data[i][j]].append((i,j))

antinodes = set()
for key in freq:
    for a0, a1 in it.combinations(freq[key],2):
        if inbounds((a1[0]-a0[0])+a1[0],0,len(data[0])-1) and inbounds((a1[1]-a0[1])+a1[1],0,len(data)-1):
            antinodes.add(((a1[0]-a0[0])+a1[0],(a1[1]-a0[1])+a1[1]))
        if inbounds((a0[0]-a1[0])+a0[0],0,len(data[0])-1) and inbounds((a0[1]-a1[1])+a0[1],0,len(data)-1):
            antinodes.add(((a0[0]-a1[0])+a0[0],(a0[1]-a1[1])+a0[1]))

prco(len(antinodes))