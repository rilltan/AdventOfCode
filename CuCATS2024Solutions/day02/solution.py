import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))[0]

out = ""
num = 0
i=25
for char in data:
    if char.isalpha():
        out += chr((ord(char)-97+i)%26 + 97)
    else:
        out += char
    i-=1
    num += 1
    if num%16 == 0:
        i-=10


print(out)