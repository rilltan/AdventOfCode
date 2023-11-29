import re
inputfile = open("day04.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()
result = 0

for x in lines:
    x = re.split(',|-',x)
    print(x)
    if (int(x[0])<=int(x[2]) and int(x[1])>=int(x[3])):
        result += 1
    elif (int(x[0])>=int(x[2]) and int(x[1])<=int(x[3])):
        result+=1

print(result)