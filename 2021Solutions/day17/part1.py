import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

x1,x2,y1,y2 = getints(data[0])

prco((-y1-1)*(-y1)//2)