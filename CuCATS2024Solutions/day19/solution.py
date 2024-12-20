import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

s1 = getints(data[1])
s2 = getints(data[2])

o1 = {}
o2 = {}
for s in s1:
    if s not in o1:
        o1[s] = 0
    if s not in o2:
        o2[s] = 0
    o1[s] += 1
for s in s2:
    if s not in o2:
        o2[s] = 0
    if s not in o1:
        o1[s] = 0
    o2[s] += 1

morein1 = []
morein2 = []
for i in o1:
    if i in o1 and o1[i] > o2[i]:
        morein1.append((i,(o1[i]-o2[i])//2))
        continue
    if i in o1 and o1[i] < o2[i]:
        morein2.append((i,(o2[i]-o1[i])//2))
        continue

morein1 = sorted(morein1,key=lambda x:x[0])
morein2 = sorted(morein2,key=lambda x:x[0])

prco(sum(x[1] for x in morein1) + sum(x[1] for x in morein2)-1)