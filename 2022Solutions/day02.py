inputfile = open("day2.txt")
result = 0
lines = list(map(lambda a: a.strip(), inputfile.readlines()))
inputfile.close()

letters1 = ["X","Y","Z"]
letters2 = ["C","A","B"]
letters3 = ["A","B","C"]

lose = [3,1,2]
draw = [1,2,3]
win = [2,3,1]

for x in lines:
    if (x[2] == "X"):
        result += lose[letters3.index(x[0])]
    if (x[2] == "Z"):
        result += win[letters3.index(x[0])]
        result += 6
    elif (x[2] == "Y"):
        result += draw[letters3.index(x[0])]
        result += 3 
        

print(result)