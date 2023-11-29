inputfile = open("day03.txt")
result = 0
lines = list(map(lambda a: a.strip(), inputfile.readlines()))
inputfile.close()

for x in range(int(len(lines)/3)):
    for letter in lines[x*3]:
        if letter in lines[x*3+1] and letter in lines[x*3+2]:
            print(letter)
            if letter.isupper():
                result += ord(letter) - 38
            else:
                result += ord(letter) - 96
            break

print(result)