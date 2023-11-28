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

pos = list(next(iter(grid)))
facing = 0
for i in path:
    if i in {"L","R"}:
        facing = (facing+{"L":-1,"R":1}[i])%4
    else:
        for j in range(int(i)):
            if facing == 0:
                pos[0] += 1
                if (pos[0],pos[1]) not in grid:
                    pos[0] = min([a for a,b in grid if b==pos[1]])
            elif facing == 1:
                pos[1] += 1
                if (pos[0],pos[1]) not in grid:
                    pos[1] = min([b for a,b in grid if a==pos[0]])
            elif facing == 2:
                pos[0] -= 1
                if (pos[0],pos[1]) not in grid:
                    pos[0] = max([a for a,b in grid if b==pos[1]])
            elif facing == 3:
                pos[1] -= 1
                if (pos[0],pos[1]) not in grid:
                    pos[1] = max([b for a,b in grid if a==pos[0]])
            if grid[pos[0],pos[1]] == "#":
                pos = list(prev)
            prev = list(pos)
print(1000*pos[1] + 4*pos[0] + facing)