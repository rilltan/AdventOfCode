import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

numpad = {"A":(3,2), "0":(3,1), "1":(2,0), "2":(2,1), "3":(2,2), "4":(1,0), "5":(1,1), "6":(1,2), "7":(0,0), "8":(0,1), "9":(0,2)}
def num_keypad_paths(a,b):
    start = numpad[a]
    end = numpad[b]
    ways = [">","<","v","^"]
    done = []
    while not done:
        for path in ways:
            x = start
            for c in path:
                x = (x[0]+u_dirsV[c][0],x[1]+u_dirsV[c][1])
                if x==(3,0):
                    break
            if x == end:
                done.append(path)
        l = len(ways)
        for i in range(l):
            ways.append(ways[i]+"<")
            ways.append(ways[i]+">")
            ways.append(ways[i]+"v")
            ways[i] = ways[i] + "^"
    return done


def num_keypad(x):
    ways = [a+"A" for a in num_keypad_paths("A",x[0])]
    for i in range(len(x)-1):
        newways = []
        for w in ways:
            for path in num_keypad_paths(x[i],x[i+1]):
                newways.append(w + path + "A")
        ways = newways.copy()
    return ways

dir_keypad_paths = {("<","v"):[">"], ("<","^"):[">^"], ("<",">"):[">>"], ("<","A"):[">>^"],
             ("v","<"):["<"], ("v",">"):[">"], ("v","^"):["^"], ("v","A"):["^>",">^"],
             ("^","<"):["v<"], ("^","v"):["v"], ("^",">"):["v>",">v"],("^","A"):[">"],
             (">","<"):["<<"],(">","v"):["<"],(">","^"):["<^","^<"],(">","A"):["^"],
             ("A","<"):["v<<"],("A","^"):["<"],("A","v"):["<v","v<"],("A",">"):["v"],
             (">",">"):[""],("<","<"):[""],("v","v"):[""],("^","^"):[""],("A","A"):[""]}

import functools
@functools.lru_cache(None)
def dir_keypad(x,y,levels):
    if levels == 0:
        return 1
    best = -1
    paths = dir_keypad_paths[x,y]
    for path in paths:
        path = path + "A"
        out = dir_keypad("A",path[0],levels-1)
        for i in range(len(path)-1):
            out += dir_keypad(path[i],path[i+1],levels-1)
        if best == -1:
            best = out
        best = min(best,out)
    return best

def dir_keypad_string(x,levels):
    out = dir_keypad("A",x[0],levels)
    for i in range(len(x)-1):
        out += dir_keypad(x[i],x[i+1],levels)
    return out

def ans(x):
    paths = num_keypad(x)
    return min([dir_keypad_string(a,25) for a in paths]) * int(x[:3])

prco(sum(ans(line) for line in data))
