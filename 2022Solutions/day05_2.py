import re

inputfile = open("day5.txt")

lines = [a.strip() for a in inputfile.readlines()]

inputfile.close()

result = ""


stacks = [[" ","G","T","R","W"],[" ","G","C","H","P","M","S","V","W"],[" ","C","L","T","S","G","M"],[" ","J","H","D","M","W","R","F"],[" ","P","Q","L","H","S","W","F","J"],[" ","P","J","D","N","F","M","S"],[" ","Z","B","D","F","G","C","S","J"],[" ","R","T","B"],[" ","H","N","W","L","C"]]

#stacks = [[" ","Z","N"],[" ","M","C","D"],[" ","P"]]

for x in lines:

    if x[0] == "m":

        x = x[5::1]

        x = re.split(" from | to ",x)

        x = [int(a)-1 for a in x]

        x[0] = x[0]+1

        for i in range(x[0]):

            stacks[x[2]].append(stacks[x[1]][-1*x[0]+i])

            stacks[x[1]].pop(-1*x[0]+i)


for i in stacks:
    print(epic(i))

    result+=i[-1]


print(result)