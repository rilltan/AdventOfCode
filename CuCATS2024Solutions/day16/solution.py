import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

songs = [[] for i in range(int(data[0]))]
j=2
for i in range(int(data[0])):
    while j<len(data) and data[j].isalpha():
        songs[i].append(data[j])
        j += 1
    j+=1

def fragments(song):
    target = song[0]
    pieces = song[1:]
    i = 0
    out = 0
    while i < len(target):
        for j in range(max(len(x) for x in pieces),0,-1):
            possible = [x[-j:] for x in pieces if len(x)>=j]
            if any(target[i:i+j] == x for x in possible):
                out += 1
                i += j
                break
    return out

prco(sum(fragments(x) for x in songs))