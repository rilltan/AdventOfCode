import os
import sys
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
numbersreversed = {x[::-1]:y for x,y in numbers.items()}
for i in range(1,10):
    numbers[str(i)] = i
    numbersreversed[str(i)] = i

result = 0
for line in data:
    linereversed = line[::-1]
    result += numbers[re.search("|".join(numbers),line).group()]*10
    result += numbersreversed[re.search("|".join(numbersreversed),linereversed).group()]

prco(result)