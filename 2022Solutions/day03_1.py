inputfile = open("day3.txt")
result = 0
lines = list(map(lambda a: a.strip(), inputfile.readlines()))
inputfile.close()

for x in lines:
    a = int(len(x)/2)
    half1 = x[0:a]
    half2 = x[a::1]
    for letter in half1:
        if letter in half2:
            print(letter)
            if letter.isupper():
                result += ord(letter) - 38
            else:
                result += ord(letter) - 96
            break

print(result)