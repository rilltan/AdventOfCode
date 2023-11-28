import math
inputfile = open("day17.txt")
jets = [a.strip() for a in inputfile.readlines()][0]
inputfile.close()

def printRocks(rocks):
    print("-")
    for y in range(max([y for x,y in rocks]),-1,-1):
            for x in range(0,7):
                if (x,y) in rocks:
                    print("#",end="")
                else:
                    print(" ",end="")
            print()
    print("-")

rockShapes = [[(0,0),(1,0),(2,0),(3,0)],[(1,0),(0,1),(1,1),(2,1),(1,2)],[(0,0),(1,0),(2,0),(2,1),(2,2)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(0,1),(1,1)]]
rockHeights = [1,3,3,4,2]
rockWidths = [4,3,3,1,2]
rock = -1
rocks = {(0,-1):1,(1,-1):1,(2,-1):1,(3,-1):1,(4,-1):1,(5,-1):1,(6,-1):1}
currentHeight = -1
currentJet = -1
move = {">":1,"<":-1}
moveBack = {">":-1,"<":1}
states = {}
found = False
foundNext = False
z=0
repeatRocks = 0
rocksBefore = 0
flag = True
while (not found or not foundNext) or flag:
    rock += 1
    if rock > 4:
        rock = 0
    falling = True
    coords = [[a,b] for a,b in rockShapes[rock]]
    for i in range(len(coords)):
        coords[i][0] += 2
        coords[i][1] += currentHeight + 4
    
    newrocks = []
    for i in rocks:
        if i[1] >= currentHeight-10:
            newrocks.append(str(i[0]))
    state = (int("".join(newrocks)),rock,currentJet)
    rocksBefore += 1
    if foundNext:
        repeatRocks-=1
        rocksBefore-=1
        z+=1
        if z>=addedCycles:
            flag = False
    if not found:
        if state in states:
            found = True
            repeated = state
            firstPos = currentHeight
    else:
        repeatRocks += 1
        if state == repeated:
            repeatHight = currentHeight-firstPos
            heightBefore = currentHeight
            addedCycles = 1000000000000-(((1000000000000//repeatRocks)-2)*repeatRocks+rocksBefore)
            foundNext = True
    states[(int("".join(newrocks)),rock,currentJet)] = 1
    
    while falling:
        currentJet += 1
        if currentJet >= len(jets):
            currentJet = 0
        wall = False
        for i in range(len(coords)):
            coords[i][0] += move[jets[currentJet]]
            if coords[i][0] > 6 or coords[i][0] < 0 or (coords[i][0],coords[i][1]) in rocks:
                wall = True
        if wall:
            for i in range(len(coords)):
                coords[i][0] += moveBack[jets[currentJet]]
        floor = False
        for i in range(len(coords)):
            coords[i][1] -= 1
            if (coords[i][0],coords[i][1]) in rocks:
                floor = True
        if floor:
            for i in range(len(coords)):
                coords[i][1] += 1
            for i in range(len(coords)):
                rocks[coords[i][0],coords[i][1]] = 1
            falling = False
    currentHeight = max([y for x,y in rocks])

print((currentHeight)+((1000000000000//repeatRocks)-2)*repeatHight+1)