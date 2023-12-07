import os
import sys
from functools import cmp_to_key
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

cards = [x.split()[0] for x in data]
bids = {x.split()[0]:int(x.split()[1]) for x in data}

strengths = {"A":13, "K":12, "Q":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2, "J":1}
strengthslist = [x for x in strengths if x!="J"]
def compare(card1:str,card2:str):
    occurs1 = []
    occurs2 = []
    for letter in strengthslist:
        occurs1.append(card1.count(letter))
        occurs2.append(card2.count(letter))
    occurs1[occurs1.index(max(occurs1))] += card1.count("J")
    occurs2[occurs2.index(max(occurs2))] += card2.count("J")

    if max(occurs1)>max(occurs2):
        return 1
    elif max(occurs2)>max(occurs1):
        return -1
    elif occurs1.count(3) == 1 and occurs1.count(2) == 1 and occurs2.count(2) == 0:
        return 1
    elif occurs2.count(3) == 1 and occurs2.count(2) == 1 and occurs1.count(2) == 0:
        return -1
    elif occurs1.count(2) > occurs2.count(2):
        return 1
    elif occurs1.count(2) < occurs2.count(2):
        return -1
    
    for i in range(5):
        if strengths[card1[i]] - strengths[card2[i]] != 0:
            return strengths[card1[i]] - strengths[card2[i]]
    return 0

sortedcards = sorted(cards,key=cmp_to_key(compare))

result = 0
for i in range(len(cards)):
    result += (i+1)*bids[sortedcards[i]]
prco(result)