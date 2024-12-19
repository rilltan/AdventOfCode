import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

level = 1
groups = [[(0,90)],[(0, 12), (13, 18), (19, 19), (20, 23), (24, 26), (27, 33), (34, 39), (40, 52), (53, 59), (60, 62), (63, 78), (79, 90)]]
flag = 2
while level<max(len(x) for x in data):
    groups.append([])
    current_group = 0
    for i,j in groups[-2]:
        groups[-1].append((i,i))
        found = False
        if len(data[i]) > level:
            found = True
        for k in range(i+1,j+1):
            if len(data[k]) <= level:
                continue
            found = True
            if len(data[k-1]) <= level:
                groups[-1].append((k,k))
                continue
            if data[k][level] == data[k-1][level]:
                groups[-1][-1] = (groups[-1][-1][0],k)
            else:
                groups[-1].append((k,k))
        if not found:
            groups[-1].pop()

    level += 1


orders = []
for k,g in enumerate(groups):
    for i,j in g:
        order = [x[k] for x in data[i:j+1] if len(x)>k]
        neworder = []
        for c in order:
            if c not in neworder:
                neworder.append(c)
        if len(neworder)>1:
            orders.append(neworder)

after = {}
before = {}
for o in orders:
    print("".join(o))
    for i,c in enumerate(o):
        if c not in after:
            after[c] = set()
        if c not in before:
            before[c] = set()
        after[c] = after[c].union(o[i+1:])
        before[c] = before[c].union(o[:i])
for c in after:
    for d in after[c]:
        before[d].add(c)
for c in before:
    for d in before[c]:
        after[d].add(c)

def score(dict):
    return sum(len(dict[x]) for x in dict)

print(score(after))
prev = -1
while prev != score(after):
    prev = score(after)
    for c in after:
        for d in after[c]:
            after[c] = after[c].union(after[d])
print(score(after))
prev = -1
while prev != score(before):
    prev = score(before)
    for c in before:
        for d in before[c]:
            before[c] = before[c].union(before[d])



outs = set()
l = "abcdefghiklmnoprstuwxyz"[::-1]
l = [x for x in l]

for abc in range(1):
    outl = []
    for c in l:
        # print(outl)
        if not outl:
            outl.append(c)
            continue
        if c not in after:
            outl.insert(0,c)
            continue
        found = False
        for i in range(len(outl)):
            # print(c,i,[x not in after[c] for x in outl[:i]])
            # print(c,i,[x not in before[c] for x in outl[i:]])
            if all([x not in after[c] for x in outl[:i]]) and all([x not in before[c] for x in outl[i:]]):
                outl.insert(i,c)
                found = True
                break
        if not found:
            outl.append(c)
    outs.add("".join(outl))
print(outs.pop())
# print(sorted(outs)[-1])
# class MyStrOrder:
#     def __init__(self, inner):
#         self.inner = inner
#         self.POS = {c:p for (p, c) in enumerate("bkrueawctpdgnoilfsmhxyz")}

#     def __lt__(self, other):
#         for i in range(min(len(self.inner), len(other.inner))):
#             a = self.POS.get(self.inner[i])
#             b = self.POS.get(other.inner[i])
#             if a != b:
#                 return a < b
#         return len(self.inner) < len(other.inner)

# random.shuffle(data)
# data.sort(key = MyStrOrder)
# for line in data:
#     print(line)