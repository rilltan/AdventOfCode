import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))


currentstate = makegrid(len(data[0]),len(data),"")
for r in range(len(data)):
    for c in range(len(data[0])):
        currentstate[r][c] = data[r][c]

def getgroup(round,empty,addhash,dir):
    start = "#" if addhash else ""
    if dir == 0 or dir == 1:
        return start + "O"*round + "."*empty
    else:
        return start + "."*empty + "O"*round

states = []
index = 0
while index==0:
    for dir in range(4):
        if dir == 0 or dir == 2:
            for c in range(len(data[0])):
                round=0
                empty=0
                column = ""
                addhash = False
                for r in range(0,len(data)):
                    if currentstate[r][c] == "O":
                        round+=1
                    elif currentstate[r][c] == ".":
                        empty+=1
                    else:
                        column += getgroup(round,empty,addhash,dir)
                        round=0
                        empty=0
                        addhash = True
                column += getgroup(round,empty,addhash,dir)
                for r in range(len(data)):
                    currentstate[r][c] = column[r]
        elif dir == 1 or dir==3:
            for r in range(len(data)):
                round=0
                empty=0
                row = ""
                addhash = False
                for c in range(len(data[0])):
                    if currentstate[r][c] == "O":
                        round+=1
                    elif currentstate[r][c] == ".":
                        empty+=1
                    else:
                        row += getgroup(round,empty,addhash,dir)
                        round=0
                        empty=0
                        addhash = True
                row += getgroup(round,empty,addhash,dir)
                for c in range(len(data)):
                    currentstate[r][c] = row[c]

    toadd = "".join(flatten(currentstate))
    if toadd in states:
        index = states.index(toadd)
        found = True
    else:
        states.append("".join(flatten(currentstate)))

indexneeeded = (1000000000-index) % (len(states)-index) + index-1
result = 0
for i in range(len(data)):
    row = states[indexneeeded][i*len(data[0]):(i+1)*(len(data[0]))]
    for j in range(len(row)):
        if row[j] == "O":
            result += len(row)-i

prco(result)