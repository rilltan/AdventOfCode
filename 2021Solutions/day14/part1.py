import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

template = data[0]
rules = {x.split(" -> ")[0]:x.split(" -> ")[1] for x in data[2:]}

for i in range(20):
    positions = []
    pos = 0
    while pos < len(template):
        if template[pos:pos+2] in rules:
            template = template[:pos+1] + rules[template[pos:pos+2]] + template[pos+1:]
            pos += 1
        pos += 1

counts = [template.count(x) for x in set(template)]
print(max(counts)-min(counts))