import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
for i in range(1,10):
    numbers[str(i)] = i

result = 0
for line in data:
    stuff = findalloverlap("|".join(numbers),line)
    if stuff:
        result += numbers[stuff[0]]*10 + numbers[stuff[-1]]

prco(result)