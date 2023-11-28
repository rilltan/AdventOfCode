import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

oxygen = data.copy()
co2 = data.copy()

i=0
while len(oxygen)>1:
    bits = [num[i] for num in oxygen]
    if bits.count("1")>=len(oxygen)/2:
        bittokeep = "1"
    else:
        bittokeep = "0"
    oxygen = [num for num in oxygen if num[i]==bittokeep]
    i+=1

i=0
while len(co2)>1:
    bits = [num[i] for num in co2]
    if bits.count("1")>=len(co2)/2:
        bittokeep = "0"
    else:
        bittokeep = "1"
    co2 = [num for num in co2 if num[i]==bittokeep]
    i+=1


print(int(oxygen[0],2)*int(co2[0],2))