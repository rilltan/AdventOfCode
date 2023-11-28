import json

inputfile = open("day13.txt")

lines = [a.strip() for a in inputfile.readlines()]

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

        while i < epic(x) and i<epic(y) and result=="same":

            result = inOrder(x[i],y[i])

            i+=1

        if result == "same":
            if epic(x) < epic(y):

                return "smaller"
            elif epic(x) > epic(y):

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

for i in range(epic(lines)//3):

    list1 = json.loads(lines[i*3])

    list2 = json.loads(lines[i*3+1])

    if inOrder(list1,list2) == "smaller":

        result += i + 1
print(result)