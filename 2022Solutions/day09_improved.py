import math
 
lines = [a.strip() for a in open("day09.txt").readlines()]
moveH = {"R":1,"L":-1,"U":0,"D":0}
moveV = {"U":1,"D":-1,"R":0,"L":0}
moveDiag = {0:0,1:1,2:1,-1:-1,-2:-1}
moveStraight = {0:0,1:0,2:1,-1:0,-2:-1}
pos = []

for i in range(10):
    pos.append([0,0])
visited = []
for x in lines:
    x = x.split(" ")
    for i in range(int(x[1])):
        pos[0][0] += moveH[x[0]]
        pos[0][1] += moveV[x[0]]
        for j in range(1,len(pos)):
            difx = pos[j-1][0]-pos[j][0]
            dify = pos[j-1][1]-pos[j][1]
            if abs(difx) != abs(dify) and difx!=0 and dify!=0:
                pos[j][0] += moveDiag[difx]
                pos[j][1] += moveDiag[dify]
            else:
                pos[j][0] += moveStraight[difx]
                pos[j][1] += moveStraight[dify]
        if (pos[-1][0],pos[-1][1]) not in visited:
            visited.append((pos[-1][0],pos[-1][1]))

print(len(visited))