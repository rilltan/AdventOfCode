import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = getints(data[0])

maxi = max(data)

costs = []
for i in range(maxi):
    cost = 0
    for j in data:
        cost += abs(i-j)
    costs.append(cost)

print(min(costs))