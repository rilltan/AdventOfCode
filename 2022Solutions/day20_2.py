inputfile = open("day20.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

original = {}
n = 0
for x in lines:
    original[n] = [int(x)*811589153,n]
    n+=1

length = len(original)
for a in range(10):
    for i in original:
        newpos = (original[i][1] + original[i][0]) % (length-1)
        if newpos == 0:
            newpos = length-1
        oldpos = original[i][1]
        original[i][1] = newpos
        if newpos > oldpos:
            for j in original:
                if original[j][1] <= newpos and original[j][1] > oldpos and j!=i:
                    original[j][1] -= 1
        elif newpos < oldpos:
            for j in original:
                if original[j][1] >= newpos and original[j][1] < oldpos and j!=i:
                    original[j][1] += 1
    print(a)
for i in original:
    if original[i][0] == 0:
        pos = original[i][1]
positions = {(1000+pos)%length,(2000+pos)%length,(3000+pos)%length}
result = 0
for i in original:
    if original[i][1] in positions:
        result += original[i][0]
print(result)