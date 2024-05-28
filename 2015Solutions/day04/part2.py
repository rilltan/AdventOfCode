import os
import sys
import hashlib
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

i = 1
while not hashlib.md5((data[0]+str(i)).encode()).hexdigest().startswith("000000"):
    i += 1

prco(i)