inputfile = open("day06.txt")
lines = [a.strip() for a in inputfile.readlines()][0]
inputfile.close()
result = 0

i=4
letters = [lines[0],lines[1],lines[2],lines[3]]
for x in range(4,len(lines)):
    i+=1
    letters.pop(0)
    letters.append(lines[x])
    if (len(set(letters)) == 1):
        print(set(letters))
        break

print(i)