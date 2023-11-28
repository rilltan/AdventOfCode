import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))
data = getints(data[0])

fish = {}
for i in range(-1,9):
    fish[i] = 0
for i in data:
    fish[i] += 1

for i in range(256):
    for j in range(9):
        fish[j-1] = fish[j]
    fish[8] = fish[-1]
    fish[6] += fish[-1]
    fish[-1] = 0
    

print(sum([fish[i] for i in fish]))