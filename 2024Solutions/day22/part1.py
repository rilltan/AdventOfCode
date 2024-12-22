import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def secret(n,it):
    for i in range(it):
        n = (n ^ (n*64)) % 16777216
        n = (n ^ (n//32)) % 16777216
        n = (n ^ (n*2048)) % 16777216
    return n
prco(sum(secret(getints(x)[0],2000) for x in data))