inputfile = open("day21.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

monkeys = {}
notnumbers = set()
for x in lines:
    x = x.split(":")
    x[1] = x[1].strip()
    if x[1].isnumeric():
        monkeys[x[0]] = int(x[1])
    else:
        notnumbers.add(x[0])
        expression = x[1].split(" ")
        monkeys[x[0]] = f"monkeys['{expression[0]}']{expression[1]}monkeys['{expression[2]}']"

while "root" in notnumbers:
    removed = []
    for x in notnumbers:
        try:
            num = eval(monkeys[x])
            if isinstance(num,int) or isinstance(num,float):
                removed.append(x)
                monkeys[x] = num
        except:
            num = 0
    for x in removed:
        notnumbers.remove(x)
print(int(monkeys["root"]))