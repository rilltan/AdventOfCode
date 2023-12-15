import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

def hash(text):
    num = 0
    for letter in text:
        num += ord(letter)
        num *= 17
        num = num % 256
    return num

prco(sum([hash(x) for x in data[0].split(",")]))