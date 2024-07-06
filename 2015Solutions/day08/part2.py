import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def encodedLength(x:str):
    return 2 + len(x) + x.count('"') + x.count("\\")

prco(sum(encodedLength(x) for x in data) - sum(len(x) for x in data))