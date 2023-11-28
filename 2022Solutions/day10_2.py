inputfile = open("day10.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()
result = 0

xreg = 1
cycle = 0
sprite = 1

for x in lines:
    x = x.split(" ")
    if x[0] == "addx":
        cycle+=1
        if (cycle-1)%40 >= sprite-1 and (cycle-1)%40 <= sprite+1:
            print("#",end="")
        else:
            print(" ",end="")
        if (cycle)%40 == 0 and cycle!=1:
            print()
        cycle += 1
        if (cycle-1)%40 >= sprite-1 and (cycle-1)%40 <= sprite+1:
            print("#",end="")
        else:
            print(" ",end="")
        if (cycle)%40 == 0:
            print()
        xreg += int(x[1])
        sprite = xreg
    elif x[0] == "noop":
        cycle += 1
        if (cycle-1)%40 >= sprite-1 and (cycle-1)%40 <= sprite+1:
            print("#",end="")
        else:
            print(" ",end="")
        if (cycle)%40 == 0:
            print()