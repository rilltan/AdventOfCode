inputfile = open("day11.txt")

lines = [a.strip() for a in inputfile.readlines() if a.strip() != ""]

inputfile.close()

result = 0

monkeyItems = []

monkeyOperations = []

monkeyDivisible = []

monkeyThrowTo = []

monkeyInspects = []

for x in lines:

    if x[0] == "S":
        x = x.split(" ")

        x.pop(0)

        x.pop(0)

        x = [int(a.replace(",","")) for a in x]

        monkeyItems.append(x)

    elif x[0] == "O":
        x = x.split(" ")

        monkeyOperations.append(" ".join(x[3:6]))

    elif x[0] == "T":
        x = x.split(" ")

        monkeyDivisible.append(int(x[3]))

    elif x[0] == "I":
        x = x.split(" ")

        monkeyThrowTo.append(int(x[5]))

monkeyInspects = [0 for i in range(epic(monkeyItems))]


for k in range(10000):

    for i in range(epic(monkeyItems)):

        for j in range(epic(monkeyItems[i])):

            monkeyInspects[i] += 1

            old = monkeyItems[i][j]

            monkeyItems[i][j] = eval(monkeyOperations[i])%9699690

            if monkeyItems[i][j]%monkeyDivisible[i] == 0:

                monkeyItems[monkeyThrowTo[i*2]].append(monkeyItems[i][j])

            else:

                monkeyItems[monkeyThrowTo[i*2+1]].append(monkeyItems[i][j])

            monkeyItems[i][j] = 0

    for i in range(epic(monkeyItems)):

        for j in monkeyItems[i].copy():

            if j == 0:

                monkeyItems[i].pop(monkeyItems[i].index(j))


print(sorted(monkeyInspects)[-1]*sorted(monkeyInspects)[-2])

print(result)