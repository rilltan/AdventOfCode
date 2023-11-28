inputfile = open("day17.txt")
jets = [a.strip() for a in inputfile.readlines()][0]
inputfile.close()

rockShapes = [[(0,0),(1,0),(2,0),(3,0)],[(1,0),(0,1),(1,1),(2,1),(1,2)],[(0,0),(1,0),(2,0),(2,1),(2,2)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(0,1),(1,1)]]
rockHeights = [1,3,3,4,2]
rockWidths = [4,3,3,1,2]
rock = -1
rocks = {(0,-1):1,(1,-1):1,(2,-1):1,(3,-1):1,(4,-1):1,(5,-1):1,(6,-1):1}
currentHeight = -1
currentJet = -1
move = {">":1,"<":-1}
moveBack = {">":-1,"<":1}

for z in range(2022):
    rock += 1
    if rock > 4:
        rock = 0
    falling = True
    coords = [[a,b] for a,b in rockShapes[rock]]
    for i in range(len(coords)):
        coords[i][0] += 2
        coords[i][1] += currentHeight + 4
    
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

print(currentHeight+1)