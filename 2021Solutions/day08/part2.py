import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

data = [["".join(sorted(y)) for y in x.split(" ")] for x in data]
letterstonum = {"abcefg":"0","cf":"1","acdeg":"2","acdfg":"3","bcdf":"4","abdfg":"5","abdefg":"6","acf":"7","abcdefg":"8","abcdfg":"9"}
simplelettermap = {4:"e",6:"b",9:"f"}
sum = 0
for line in data:
    wiremap = {x:"" for x in "abcdefg"}
    letterfreq = {x:flatten(line[0:10]).count(x) for x in wiremap}

    for letter in letterfreq:
        if letterfreq[letter] in simplelettermap:
            wiremap[letter] = simplelettermap[letterfreq[letter]]
    for signal in line[0:10]:
        if len(signal) == 2:
            for x,y in wiremap.items():
                if y == "f":
                    letter1 = x
                    break
            signalstring = signal.replace(letter1,"")
            wiremap[signalstring] = "c"
    for signal in line[0:10]:
        if len(signal) == 4:
            toremove = ""
            for x,y in wiremap.items():
                if y=="b" or y=="c" or y=="f":
                    toremove += x
            lastletter = re.sub(f"{toremove[0]}|{toremove[1]}|{toremove[2]}","",signal)
            wiremap[lastletter] = "d"

    for letter in letterfreq:
        if letterfreq[letter] == 8 and wiremap[letter] == "":
            wiremap[letter] = "a"
        elif letterfreq[letter] == 7 and wiremap[letter] == "":
            wiremap[letter] = "g"
    
    outputnum = ""
    for signal in line[11:15]:
        outputnum += letterstonum["".join(sorted([wiremap[x] for x in signal]))]
    sum += int(outputnum)

print(sum)