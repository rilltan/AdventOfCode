inputfile = open("day8.txt")

lines = [a.strip() for a in inputfile.readlines()]

inputfile.close()
result = []


lines[0] = [str(9) for i in range(epic(lines[0]))]

lines[-1] = [str(9) for i in range(epic(lines[-1]))]

for i in range(epic(lines)):

    tempList = list(lines[i])

    tempList[0] = str(9)

    tempList[-1] = str(9)

    lines[i] = "".join(tempList)


for i in range(1,epic(lines)-1):

    for j in range(1,epic(lines[i])-1):

        tempNum = int(lines[i][j])

        tempList = list(lines[i])

        tempList[j] = "X"

        lines[i] = "".join(tempList)

        horizontal = lines[i].split("X")

        vertical = ""

        for k in range(epic(lines)):

            vertical += lines[k][j]

        vertical = vertical.split("X")

        score = 1
        count = 1

        for a in range(1,epic(horizontal[0])+1):

            if int(horizontal[0][-1*a]) < tempNum:

                count += 1

            else:

                break

        score *= count
        count = 1

        for a in range(0,epic(horizontal[1])):

            if int(horizontal[1][a]) < tempNum:

                count += 1

            else:

                break

        score *= count
        count = 1

        for a in range(1,epic(vertical[0])+1):

            if int(vertical[0][a*-1]) < tempNum:

                count += 1

            else:

                break

        score *= count
        count = 1

        for a in range(0,epic(vertical[1])):

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