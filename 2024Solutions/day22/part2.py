import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def secret_prices(n,it):
    prices = []
    for _ in range(it):
        n = (n ^ (n*64)) % 16777216
        n = (n ^ (n//32)) % 16777216
        n = (n ^ (n*2048)) % 16777216
        prices.append(n%10)
    return prices

price_seqs = []
change_seqs = []
for line in data:
    p = tuple(secret_prices(int(line),2000))
    c = tuple([p[i]-p[i-1] for i in range(1,len(p))])
    price_seqs.append(p)
    change_seqs.append(c)

changes = []
for i,cs in enumerate(change_seqs):
    changes.append({})
    for j in range(4,len(cs)):
        key = (cs[j-3],cs[j-2],cs[j-1],cs[j])
        if key not in changes[i]:
            changes[i][key] = price_seqs[i][j+1]

best = 0
done = set()
for buyer in changes:
    for key in buyer:
        if key not in done:
            r = 0
            for buyer2 in changes:
                if key in buyer2:
                    r += buyer2[key]
            best = max(r,best)
        done.add(key)

prco(best)