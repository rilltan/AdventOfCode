import json
inputfile = open("day13.txt")
lines1 = [a.strip() for a in inputfile.readlines() if a!="\n"]
lines = [json.loads(a) for a in lines1]
inputfile.close()

def inOrder(x,y):
    if isinstance(x,int) and isinstance(y,int):
        if x<y:
            return "smaller"
        elif x>y:
            return "larger"
        else:
            return "same"
    elif isinstance(x,list) and isinstance(y,list):
        result = "same"
        i=0
        while i < len(x) and i<len(y) and result=="same":
            result = inOrder(x[i],y[i])
            i+=1
        if result == "same":
            if len(x) < len(y):
                return "smaller"
            elif len(x) > len(y):
                return "larger"
            else:
                return "same"
        else:
            return result
    else:
        if isinstance(x,int):
            x = [x]
        elif isinstance(y,int):
            y = [y]
        return inOrder(x,y)

result = 0
sortedLines = []
length = len(lines)
for a in range(length):
    smallest = lines[0]
    smallestIndex = 0
    for j,i in enumerate(lines):
        if inOrder(i,smallest) == "smaller":
            smallest = list(i)
            smallestIndex = j
    sortedLines.append(smallest)
    lines.pop(smallestIndex)

print((sortedLines.index([[2]])+1) * (sortedLines.index([[6]])+1))