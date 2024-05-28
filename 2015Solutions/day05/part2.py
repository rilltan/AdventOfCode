import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

vowels = set(["a","e","i","o","u"])
forbidden = ["ab","cd","pq","xy"]

def nice(x:str):
    x += " "
    double = False
    for i in range(len(x)-2):
        if x[i:i+2] in x[:i] or x[i:i+2] in x[i+2:]:
            double = True
            break
    repeat = any([x[i]==x[i+2] for i in range(len(x)-3)])
    return double and repeat

prco(len([x for x in data if nice(x)]))