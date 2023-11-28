inputfile = open("day22.txt")
lines = [a for a in inputfile.readlines()]
inputfile.close()

grid = {}
for y,i in enumerate(lines):
    for x,j in enumerate(i):
        if j in {".","#"}:
            grid[x+1,y+1] = j
oldpath = lines[-1].strip() + "A"
prev = ""
toadd = ""
path = []
for i in oldpath:
    if prev.isalpha() != i.isalpha():
        path.append(toadd)
        toadd = i
    else:
        toadd += i
    prev = i

move = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
pos = list(next(iter(grid)))
facing = 0
for i in path:
    if i in {"L","R"}:
        facing = (facing+{"L":-1,"R":1}[i])%4
    else:
        for j in range(int(i)):
            pos[0] += move[facing][0]
            pos[1] += move[facing][1]

            if (pos[0],pos[1]) not in grid:
                if facing == 0: # right
                    if pos[1] <= 50: # 1
                        pos[0] = 100
                        pos[1] = 151 - pos[1]
                        facing = 2
                    elif pos[1] <= 100: # 3
                        pos[0] = pos[1] + 50
                        pos[1] = 50
                        facing = 3
                    elif pos[1] <= 150: # 4
                        pos[0] = 150
                        pos[1] = 151 - pos[1]
                        facing = 2
                    else: # 6
                        pos[0] = pos[1] - 100
                        pos[1] = 150
                        facing = 3
                elif facing == 1: # down
                    if pos[0] <= 50: # 6
                        pos[1] = 1
                        pos[0] = pos[0] + 100
                        facing = 1
                    elif pos[0] <= 100: # 4
                        pos[1] = pos[0] + 100
                        pos[0] = 50
                        facing = 2
                    else: # 1
                        pos[1] = pos[0] - 50
                        pos[0] = 100
                        facing = 2
                elif facing == 2: # left
                    if pos[1] <= 50: # 2
                        pos[0] = 1
                        pos[1] = 151 - pos[1]
                        facing = 0
                    elif pos[1] <= 100: # 3
                        pos[0] = pos[1] - 50
                        pos[1] = 101
                        facing = 1
                    elif pos[1] <= 150: # 5
                        pos[0] = 51
                        pos[1] = 151 - pos[1]
                        facing = 0
                    else: # 6
                        pos[0] = pos[1] - 100
                        pos[1] = 1
                        facing = 1
                else: # up
                    if pos[0] <= 50: # 5
                        pos[1] = pos[0] + 50
                        pos[0] = 51
                        facing = 0
                    elif pos[0] <= 100: # 2
                        pos[1] = pos[0] + 100
                        pos[0] = 1
                        facing = 0
                    else: # 1
                        pos[1] = 200
                        pos[0] = pos[0] - 100
                        facing = 3
            if grid[pos[0],pos[1]] == "#":
                pos = list(prev)
            prev = list(pos)
print(1000*pos[1] + 4*pos[0] + facing)