inputfile = open("day21.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

monkeys = {}
for x in lines:
    x = x.split(":")
    x[1] = x[1].strip()
    if x[1].isnumeric():
        monkeys[x[0]] = int(x[1])
    else:
        expression = x[1].split(" ")
        monkeys[x[0]] = f"monkeys['{expression[0]}']{expression[1]}monkeys['{expression[2]}']"

def calculate(monkeys1):
    monkeys = {}
    for x in monkeys1:
        monkeys[x] = monkeys1[x]
    notnumbers = set()
    for x in monkeys:
        if isinstance(monkeys[x],str):
            notnumbers.add(x)
    notnumbers.remove("root")
    while notnumbers:
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
    return monkeys

monkeys["humn"] = 3451534022348
monkeysCalculated = calculate(monkeys)
print(monkeysCalculated[monkeys["root"][9:13]])
print(monkeysCalculated[monkeys["root"][25:29]])