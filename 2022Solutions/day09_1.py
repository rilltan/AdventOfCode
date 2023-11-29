inputfile = open("day09.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()
result = 0

hPos = [0,0]
tPos = [0,0]
visitedPoints = []

for x in lines:
    x = x.split(" ")
    for i in range(int(x[1])):
        if x[0] == "R":
            hPos[0]+=1
        elif x[0] == "U":
            hPos[1] -= 1
        elif x[0] == "L":
            hPos[0] -= 1
        elif x[0] == "D":
            hPos[1] += 1

        diagonal = False
        if hPos[0] != tPos[0] and hPos[1] != tPos[1]:
            diagonal = True
        touching = True
        if tPos[0] < hPos[0]-1 or tPos[0]>hPos[0]+1 or tPos[1]<hPos[1]-1 or tPos[1]>hPos[1]+1:
            touching = False

        if not touching:
            if not diagonal:
                if x[0] == "R":
                    tPos[0]+=1
                elif x[0] == "U":
                    tPos[1] -= 1
                elif x[0] == "L":
                    tPos[0] -= 1
                elif x[0] == "D":
                    tPos[1] += 1
            else:
                if x[0] == "U":
                    tPos[0] = hPos[0]
                    tPos[1] = hPos[1] + 1
                elif x[0] == "D":
                    tPos[0] = hPos[0]
                    tPos[1] = hPos[1] - 1
                elif x[0] == "R":
                    tPos[1] = hPos[1]
                    tPos[0] = hPos[0] - 1
                elif x[0] == "L":
                    tPos[1] = hPos[1]
                    tPos[0] = hPos[0] + 1

        if (tPos[0],tPos[1]) not in visitedPoints:
            visitedPoints.append((tPos[0],tPos[1]))

print(len(visitedPoints))