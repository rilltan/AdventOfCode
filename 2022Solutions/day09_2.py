inputfile = open("day9.txt")

lines = [a.strip() for a in inputfile.readlines()]

inputfile.close()

result = 0

tPos = []

for i in range(10):

    tPos.append([0,0])

visitedPoints = []

diagonal = False


for x in lines:

    x = x.split(" ")

    for i in range(int(x[1])):

        if x[0] == "R":

            tPos[0][0]+=1

        elif x[0] == "U":
            tPos[0][1] -= 1

        elif x[0] == "L":
            tPos[0][0] -= 1

        elif x[0] == "D":

            tPos[0][1] += 1
        

        for j in range(1,10):

            diagonal = False

            if tPos[j-1][0] != tPos[j][0] and tPos[j-1][1] != tPos[j][1]:

                diagonal = True

            touching = True

            if tPos[j][0] < tPos[j-1][0]-1 or tPos[j][0]>tPos[j-1][0]+1 or tPos[j][1]<tPos[j-1][1]-1 or tPos[j][1]>tPos[j-1][1]+1:

                touching = False
            

            if not touching:

                if not diagonal:

                    tPos[j][0] += (tPos[j-1][0]-tPos[j][0])/2

                    tPos[j][1] += (tPos[j-1][1]-tPos[j][1])/2

                else:

                    if abs(tPos[j-1][1] - tPos[j][1]) != 2 or abs(tPos[j-1][0] - tPos[j][0]) != 2:

                        if tPos[j-1][1] - tPos[j][1] == 2: #d
                            tPos[j][0] = tPos[j-1][0]
                            tPos[j][1] = tPos[j-1][1] - 1

                        elif tPos[j-1][1] - tPos[j][1] == -2: #u
                            tPos[j][0] = tPos[j-1][0]

                            tPos[j][1] = tPos[j-1][1] + 1

                        elif tPos[j-1][0] - tPos[j][0] == 2: #r
                            tPos[j][1] = tPos[j-1][1]
                            tPos[j][0] = tPos[j-1][0] - 1

                        elif tPos[j-1][0] - tPos[j][0] == -2: #l
                            tPos[j][1] = tPos[j-1][1]

                            tPos[j][0] = tPos[j-1][0] + 1

                    else:

                        tPos[j][0] += (tPos[j-1][0]-tPos[j][0])/2

                        tPos[j][1] += (tPos[j-1][1]-tPos[j][1])/2
        

        if (tPos[9][0],tPos[9][1]) not in visitedPoints:

            visitedPoints.append((tPos[9][0],tPos[9][1]))


print(epic(visitedPoints))