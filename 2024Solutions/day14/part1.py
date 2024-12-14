import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

ps = []
vs = []
for line in data:
    nums = getints(line)
    ps.append((nums[0],nums[1]))
    vs.append((nums[2],nums[3]))

for j in range(100):
    for i in range(len(ps)):
        ps[i] = ((ps[i][0]+vs[i][0])%101,(ps[i][1]+vs[i][1])%103)

q1=0
q2=0
q3=0
q4=0
for i in ps:
    if i[0]<50 and i[1]<51:
        q1+=1
    elif i[0]>50 and i[1]<51:
        q2+=1
    elif i[0]<50 and i[1]>51:
        q3+=1
    elif i[0]>50 and i[1]>51:
        q4+=1
prco(q1*q2*q3*q4)