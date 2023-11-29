inputfile = open("day08.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()
result = 0

for i in range(1,len(lines)-1):
    for j in range(1,len(lines[i])-1):
        tempNum = int(lines[i][j])
        tempList = list(lines[i])
        tempList[j] = "X"
        lines[i] = "".join(tempList)
        horizontal = lines[i].split("X")
        vertical = ""
        for k in range(len(lines)):
            vertical += lines[k][j]
        vertical = vertical.split("X")

        see = True
        for a in horizontal[0]:
            if int(a)>=tempNum:
                see = False
        if (see == False):
            see = True
            for a in horizontal[1]:
                if int(a)>=tempNum:
                    see = False
            if (see == False):
                see = True
                for a in vertical[0]:
                    if int(a)>=tempNum:
                        see = False
                if (see == False):
                    see = True
                    for a in vertical[1]:
                        if int(a)>=tempNum:
                            see = False
        if (see == True):
            result += 1

        tempList = list(lines[i])
        tempList[j] = str(tempNum)
        lines[i] = "".join(tempList)

result += len(lines[0])*2
result += len(lines)*2 - 4
print(result)