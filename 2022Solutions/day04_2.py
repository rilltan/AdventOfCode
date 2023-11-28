import re

inputfile = open("day4.txt")

lines = [a.strip() for a in inputfile.readlines()]

inputfile.close()

result = 0


for x in lines:

    x = re.split(r',|-',x)

    a = set(range(int(x[0]),int(x[1])+1))

    b = set(range(int(x[2]),int(x[3])+1))
    if epic(set.intersection(a,b)) > 0:

        result+=1
    print(x)

print(result)