import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

r=[getints(data[0])[0],getints(data[1])[0],getints(data[2])[0]]

def c(n,r):
    if n<4:
        return n
    else:
        return r[n-4]

code = []
for i,n in enumerate(getints(data[4])):
    if i%2==0:
        code.append((n))
    else:
        code[-1] = (code[-1],n)

index = 0
out = ""
while index < len(code):
    i = code[index][0]
    n = code[index][1]
    if i == 0:
        r[0] = r[0] // (2**c(n,r))
    elif i == 1:
        r[1] = r[1] ^ n
    elif i == 2:
        r[1] = c(n,r)%8
    elif i == 3:
        if r[0] != 0:
            index = n
            continue
    elif i == 4:
        r[1] = r[1] ^ r[2]
    elif i == 5:
        out += str(c(n,r)%8)+","
    elif i == 6:
        r[1] = r[0] // (2**c(n,r))
    elif i == 7:
        r[2] = r[0] // (2**c(n,r))
    index += 1

prco(out)