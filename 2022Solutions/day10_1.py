inputfile = open("day10.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()
result = 0

xreg = 1
cycle = 0

for x in lines:
    x = x.split(" ")
    if x[0] == "addx":
        cycle+=1
        if (cycle+20)%40==0:
            result += cycle*xreg
        cycle += 1
        if (cycle+20)%40==0:
            result += cycle*xreg
        xreg += int(x[1])
    elif x[0] == "noop":
        cycle += 1
        if (cycle+20)%40==0:
            result += cycle*xreg

print(result)