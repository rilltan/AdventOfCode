import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

answers = {}
for n in getints(data[0]):
    if n not in answers:
        answers[n] = 0
    answers[n] += 1
print(answers)
out = 0
for n in answers:
    out += answers[n]
    out += (n+1-answers[n])%(n+1)

prco(out)
print(len(getints(data[0])))