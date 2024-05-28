import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

vowels = set(["a","e","i","o","u"])
forbidden = ["ab","cd","pq","xy"]

def nice(x:str):
    return (len([y for y in x if y in vowels]) >= 3
            and any(x[i] == x[i+1] for i in range(len(x)-1))
            and all(y not in x for y in forbidden))

prco(len([x for x in data if nice(x)]))