inputfile = open("day14.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

walls = []
maxx = 0
minx = 10000
maxy = 0
miny = 10000
for x in lines:
    x = x.split(" -> ")
    temp = [a.split(",") for a in x]
    temp = [(int(a),int(b)) for a,b in temp]
    maxx=max(maxx,max([a[0] for a in temp]))
    minx=min(minx,min([a[0] for a in temp]))
    maxy=max(maxy,max([a[1] for a in temp]))
    miny=min(miny,min([a[1] for a in temp]))
    walls.append(temp)
grid = {}
for i in range(0,1000):
    for j in range(0,maxy+2):
        grid[i,j] = " "

for coords in walls:
    for i in range(len(coords)-1):
        xdirection = 1 if coords[i][0] < coords[i+1][0] else -1
        for x in range(coords[i][0],coords[i+1][0]+xdirection,xdirection):
            ydirection = 1 if coords[i][1] < coords[i+1][1] else -1
            for y in range(coords[i][1],coords[i+1][1]+ydirection,ydirection):
                grid[x,y] = "#"
for x in range(0,1000):
    grid[x,maxy+2] = "#"

void = False
count = 0
while not void:
    sandx = 500
    sandy = 0
    falling = True
    while falling:
        try:
            if grid[sandx,sandy+1]==" ":
                sandy += 1
            elif grid[sandx-1,sandy+1] == " ":
                sandx -= 1
                sandy += 1
            elif grid[sandx+1,sandy+1] == " ":
                sandx += 1
                sandy += 1
            else:
                falling = False
                grid[sandx,sandy] = "o"
        except:
            void = True
            falling = False
    if not void:
        count+=1
    if sandx == 500 and sandy == 0:
        void = True

print(count)