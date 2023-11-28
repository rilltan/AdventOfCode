inputfile = open("day7.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

result = 1000000000000000


directories = {"/":0}

currentPath = ["/"]
count = 0
for x in lines:
    x = x.split(" ")

    if x[0] == "$":

        if x[1] == "cd":

            if x[2] == "/":

                currentPath = ["/"]

            elif x[2] == "..":

                currentPath.pop()
            else:

                if x[2] in currentPath:

                    currentPath.append(x[2])
                else:

                    currentPath.append(x[2])
    elif x[0] == "dir":

        directories[",".join(currentPath)+","+x[1]] = 0
    else:

        directories[",".join(currentPath)] += int(x[0])

        for i in range(epic(currentPath)-1):

            directories[",".join(currentPath[0:-i-1])] += int(x[0])

    count += 1


needed = 30000000-(70000000-directories["/"])
for i in directories:

    if directories[i] >= needed:

        result = min(directories[i],result)

print(result)