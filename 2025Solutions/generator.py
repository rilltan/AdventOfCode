import os

layout = """import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

"""
currentdir = os.path.dirname(__file__)

for i in range(1,13):
    istring = str(i).zfill(2)
    folder = os.path.join(currentdir, f"day{istring}")
    if not os.path.exists(folder):
        os.makedirs(folder)
    x = open(os.path.join(folder,"part1.py"),"w")
    x.writelines(layout)
    x.close()
    x = open(os.path.join(folder,"part2.py"),"w")
    x.writelines(layout)
    x.close()
    x = open(os.path.join(folder,"input.txt"),"w")
    x.close()