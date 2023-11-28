inputfile = open("day23.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

elves = {}
n = 0
for y,i in enumerate(lines):
    for x,j in enumerate(i):
        if j == "#":
            elves[x,y] = n
            n += 1

moveDirection = {"N":(0,-1),"S":(0,1),"E":(1,0),"W":(-1,0),"done":(0,0)}
order = ["N","S","W","E"]
done = False

a = 0
while not done:
    a += 1
    move = []

    for i in elves:
        directions = []
        if (i[0],i[1]+1) not in elves and (i[0]+1,i[1]+1) not in elves and (i[0]-1,i[1]+1) not in elves:
            directions.append("S")
        if (i[0],i[1]-1) not in elves and (i[0]+1,i[1]-1) not in elves and (i[0]-1,i[1]-1) not in elves:
            directions.append("N")
        if (i[0]-1,i[1]) not in elves and (i[0]-1,i[1]+1) not in elves and (i[0]-1,i[1]-1) not in elves:
            directions.append("W")
        if (i[0]+1,i[1]) not in elves and (i[0]+1,i[1]+1) not in elves and (i[0]+1,i[1]-1) not in elves:
            directions.append("E")
        if len(directions) == 4:
            move.append("done")
        elif not directions:
            move.append("done")
        else:
            for direction in order:
                if direction in directions:
                    move.append(direction)
                    break
    newelves = {}
    newelveslist = []
    n = 0
    for i in elves:
        newelves[i[0]+moveDirection[move[n]][0],i[1]+moveDirection[move[n]][1]] = n
        newelveslist.append((i[0]+moveDirection[move[n]][0],i[1]+moveDirection[move[n]][1]))
        n+=1
    n = 0
    finalelves = [None] * len(newelveslist)
    for i in newelveslist:
        if newelves[i] != n:
            finalelves[n] = (i[0]-moveDirection[move[n]][0],i[1]-moveDirection[move[n]][1])
            finalelves[newelves[i]] = (i[0]-moveDirection[move[newelves[i]]][0],i[1]-moveDirection[move[newelves[i]]][1])
        elif finalelves[n] == None:
            finalelves[n] = i
        n += 1
    
    elves = {}
    n = 0
    for i in finalelves:
        elves[i] = n
        n += 1
    order.append(order.pop(0))
    done = True
    for i in move:
        if i != "done":
            done = False
            break

print(a)