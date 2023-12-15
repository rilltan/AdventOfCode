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

boxes = {i:{} for i in range(256)}
for label in data[0].split(","):
    if "=" in label:
        parts = label.split("=")
        hashed = hash(parts[0])
        boxes[hashed][parts[0]] = int(parts[1])
    else:
        hashed = hash(label[:-1])
        if label[:-1] in boxes[hashed]:
            boxes[hashed].pop(label[:-1])

result = 0
for i in boxes:
    for j,x in enumerate(boxes[i]):
        result += (i+1)*(j+1)*boxes[i][x]
prco(result)