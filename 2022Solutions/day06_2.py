inputfile = open("day06.txt")
lines = [a.strip() for a in inputfile.readlines()][0]
inputfile.close()
result = 0

i=14
letters = [lines[a] for a in range(14)]
for x in range(14,len(lines)):
    i+=1
    letters.pop(0)
    letters.append(lines[x])
    if (len(set(letters)) == 14):
        print(set(letters))
        break 

print(i)