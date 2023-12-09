import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def all_zeroes(x):
    allzeroes = True
    for i in x:
        if i != 0:
            allzeroes = False
            break
    return allzeroes

seqs = [getints(x) for x in data]
result = 0

for seq in seqs:
    difs = [[x for x in seq]]
    while not all_zeroes(difs[-1]):
        difs.append([])
        for i in range(len(difs[-2])-1):
            difs[-1].append(difs[-2][i+1]-difs[-2][i])
    result += sum(x[0]*-(i%2*2-1) for i,x in enumerate(difs))

prco(result)