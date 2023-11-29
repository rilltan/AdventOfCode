inputfile = open("day01.txt")
result = 0
biggest = [0,0,0]
current = 0
pos = 0
finished = False

for x in inputfile:
    if x == "\n":
        if current > min(biggest):
            biggest[biggest.index(min(biggest))] = current
        current = 0

    else:
        current += int(x)

result = sum(biggest)
inputfile.close()
print(result)