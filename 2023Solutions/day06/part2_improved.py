import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

time = int("".join([str(x) for x in getints(data[0])]))
dist = int("".join([str(x) for x in getints(data[1])]))

upper = time
lower = 0
mid = (upper+lower)//2
while upper != mid and lower != mid:
    mid = (upper+lower)//2
    if mid * (time-mid) >= dist:
        upper = mid - 1
    else:
        lower = mid + 1
min = mid

upper = time
lower = 0
mid = (upper+lower)//2
while upper != mid and lower != mid:
    mid = (upper+lower)//2
    if mid * (time-mid) >= dist:
        lower = mid + 1
    else:
        upper = mid - 1
max = mid

for i in range(min-3,min+3):
    if i * (time-i) >= dist:
        min = i
        break
for i in range(max-3,max+3):
    if i * (time-i) < dist:
        max = i-1
        break

prco(max-min+1)