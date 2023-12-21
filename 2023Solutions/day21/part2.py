import os
import sys
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def infindex(grid,r,c):
    return 

start = (-1,-1)
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "S":
            start = (r,c)
            data[r] = data[r].replace("S",".")

full = 15221
megagrid = {}
megagridodd = {}
seen = set()
filled = set()
q = deque()
q.append(start)
num = 1

stats = {"filledgrids":[],"totaltiles":[]}
for i in range(1,1000):
    n = (i+1)//131
    newnum = 0
    for j in range(num):
        pos = q.popleft()
        for r,c in u_cardinals:
            if (pos[0]+r,pos[1]+c) not in seen and data[(pos[0]+r)%len(data)][(pos[1]+c)%len(data[0])] != "#":
                seen.add((pos[0]+r,pos[1]+c))
                q.append((pos[0]+r,pos[1]+c))
                newnum += 1

                megapos = ((pos[0]+r)//len(data),(pos[1]+c)//len(data[0]))
                if megapos not in megagrid:
                    megagrid[megapos] = 0
                megagrid[megapos] += 1
                
                if i%2==0:
                    continue
                if megapos not in megagridodd:
                    megagridodd[megapos] = 0
                megagridodd[megapos] += 1
    num = newnum

    updated = False
    for r,c in megagrid:
        if (r,c) not in filled and megagrid[r,c] == full:
            filled.add((r,c))
            updated = True
    if updated:
        stats["filledgrids"].append((i,len(filled),len([x for x in filled if (x[0]+x[1])%2==0]),len([x for x in filled if (x[0]+x[1])%2==1])))
    if i % 131 == 65:
        stats["totaltiles"].append((i,sum(megagridodd[x] for x in megagridodd),sum(megagridodd[x] for x in megagridodd if x not in filled)))

print(" n |   i | Filled | Even filled | Odd filled")
template = "{:>2}{:>6}{:>9}{:>14}{:>13}"
for i,filled,even,odd in stats["filledgrids"]:
    print(template.format((i+1)//131,i,filled,even,odd))
print()
print(" n |   i | Total tiles | Tiles in non-filled grids")
template = "{:>2}{:>6}{:>14}{:>28}"
for i,total,nonfilled in stats["totaltiles"]:
    print(template.format((i+1)//131,i,total,nonfilled))
print()

def formula(i):
    if i%131 != 65 or i%2 == 0:
        return -1
    
    n = (i+1) // 131
    tiles_in_filled = 7576 * (n-(n+1)%2)*(n-(n+1)%2) + 7645 * (n-(n)%2)*(n-(n)%2)
    if n%2 == 0:
        tiles_in_non_filled = 30490 * n - 3694
    else:
        tiles_in_non_filled = 30389 * n - 3881
    return tiles_in_non_filled + tiles_in_filled

print("Answer: ")
prco(formula(26501365))


# i = the current step
# n = (i+1) // 131
#
# All my calculations are done assuming an odd number of steps, since 26501365 is odd

# TILES IN FILLED GRIDS
# A filled grid is where the possible reachable positions are the same at i and i+2
# The number of filled grids increases every 131 steps
#
# Odd grids are grids whose mega-coordinates (r,c) satisfy (r + c) % 2 == 1
# Even grids are grids whose mega-coordinates (r,c) satisfy (r + c) % 2 == 0
# The total reachable tiles in a filled odd grid (on an odd step as specified before) is 7576
# The total reachable tiles in a filled even grid (on an odd step as specified before) is 7645
#
# By looking at the patterns in the first table printed by this program, you can derive
# number of odd grids = (most recent odd n) ^ 2 = (n-(n+1)%2)*(n-(n+1)%2)
# number of even grids = (most recent even n) ^ 2 = (n-(n)%2)*(n-(n)%2)
# => tiles in filled grids = 7576 * (n-(n+1)%2)*(n-(n+1)%2) + 7645 * (n-(n)%2)*(n-(n)%2)

# TILES IN NON-FILLED GRIDS
# 26501365 % 131 = 65, so I looked at how many reachable tiles were in non-filled grids when i % 131 == 65
# For each n, the outermost ring of filled swaps between odd and even, so I made two equations for when n is odd and when n is even
#
# I used an online calculator to do Newton's forward interpolation formula, using the data in the second table printed by this program
# x = n, f(x) = tiles in non-filled grids
# If n is even and i % 131 = 65:
#   tiles in non-filled grids = 30490 * n - 3694
# If n is odd and i % 131 = 65:
#   tiles in non-filled grids = 30389 * n - 3881

# Total = tiles in non-filled grids + tiles in filled grids