import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

template = data[0]
rules = {}
for rule in data[2:]:
    pair,result = rule.split(" -> ")
    rules[pair] = (pair[0]+result,result+pair[1])
pair_occurences = {pair:template.count(pair) for pair in rules}


for i in range(40):
    toadd = {pair:0 for pair in rules}
    for pair in pair_occurences:
        toadd[rules[pair][0]] += pair_occurences[pair]
        toadd[rules[pair][1]] += pair_occurences[pair]
        toadd[pair] -= pair_occurences[pair]
    for pair in pair_occurences:
        pair_occurences[pair] += toadd[pair]

lettercounts = {letter:0 for letter in string.ascii_uppercase}
for pair in pair_occurences:
    lettercounts[pair[0]] += pair_occurences[pair]
    lettercounts[pair[1]] += pair_occurences[pair]
lettercounts[template[0]] += 1
lettercounts[template[-1]] += 1
for letter in lettercounts:
    lettercounts[letter] //= 2 

prco((max(lettercounts.values()) - min([x for x in list(lettercounts.values()) if x != 0])))