import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

# This code doesn't work out the answer, it just prints some helpful data for me to figure it out manually

original_states = {}
for i,line in enumerate(data):
    if line == "":
        wires = data[i+1:]
        break
    original_states[line[:3]] = 1 if line.split()[1] == "1" else 0

def execute(i1,i2,i3,i4,x,y):
    states = original_states.copy()
    for i in range(45):
        states["x"+str(i).zfill(2)] = (x >> i) & 1
        states["y"+str(i).zfill(2)] = (y >> i) & 1
    last = -1
    while len(states) != last:
        last = len(states)
        for i in range(len(i1)):
            x = line.split()
            if i1[i] in states and i2[i] in states:
                if i3[i] == "XOR":
                    states[i4[i]] = states[i1[i]] ^ states[i2[i]]
                if i3[i] == "AND":
                    states[i4[i]] = states[i1[i]] & states[i2[i]]
                if i3[i] == "OR":
                    states[i4[i]] = states[i1[i]] | states[i2[i]]
    r = 0
    for i in range(46):
        r += (2**i) * states["z"+str(i).zfill(2)]
    return r

in1 = []
in2 = []
in3 = []
in4 = []
back = {}
for line in wires:
    x = line.split()
    in1.append(x[0])
    in2.append(x[2])
    in3.append(x[1])
    in4.append(x[4])
    back[x[4]] = (x[0],x[1],x[2])

x=int("101100110111111001000001001101100001011010101"[::-1],2)
y=int("100110000001001110101010000110111110110011011"[::-1],2)

def find(back,t):
    r = back[t]
    if r[0][0] != "x" and r[0][0] != "y":
        r = (find(back,r[0]),r[1],r[2])
    if r[2][0] != "x" and r[2][0] != "y":
        r = (r[0],r[1],find(back,r[2]))
    return r
import re
def stripzeroes(x):
    if x=="00" or x=="0":
        return "0"
    return x.lstrip("0")
def tts(t):
    return str(t).replace("'","").replace(",","").replace("AND","&").replace("XOR","^").replace("OR","|")
def tts2(t):
    return re.sub(r"\d+",lambda x:"["+stripzeroes(x.group())+"]",tts(t))

zs = []
for z in in4:
    if z[0]=="z":
        zs.append(z)
zs = sorted(zs)

x=[int(a) for a in "101100110111111001000001001101100001011010101"]
y=[int(a) for a in "100110000001001110101010000110111110110011011"]
x = [1 for _ in range(45)]
y = [1 for _ in range(45)]

for i,z in enumerate(zs):
    print(z+": "+str(eval(tts2(find(back,z)))))
    s = tts(find(back,z))
    if s.count("x") != i*2:
        print(z)
        print(s)
        print(back[z])

swaps = ["fkb", "z16", "rqf", "nnr", "rdn", "z31", "rrn", "z37"]
prco(",".join(sorted(swaps)))