inputfile = open("day08.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()
result = []

lines[0] = [str(9) for i in range(len(lines[0]))]
lines[-1] = [str(9) for i in range(len(lines[-1]))]
for i in range(len(lines)):
    tempList = list(lines[i])
    tempList[0] = str(9)
    tempList[-1] = str(9)
    lines[i] = "".join(tempList)

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
        score = 1
        count = 1
        for a in range(1,len(horizontal[0])+1):
            if int(horizontal[0][-1*a]) < tempNum:
                count += 1
            else:
                break
        score *= count
        count = 1
        for a in range(0,len(horizontal[1])):
            if int(horizontal[1][a]) < tempNum:
                count += 1
            else:
                break
        score *= count
        count = 1
        for a in range(1,len(vertical[0])+1):
            if int(vertical[0][a*-1]) < tempNum:
                count += 1
            else:
                break
        score *= count
        count = 1
        for a in range(0,len(vertical[1])):
            if int(vertical[1][a]) < tempNum:
                count += 1
            else:
                break
        score *= count
        count = 1

        result.append(score)
        tempList = list(lines[i])
        tempList[j] = str(tempNum)
        lines[i] = "".join(tempList)


print(max(result))