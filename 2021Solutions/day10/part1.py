import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

scores = {"(":3,"[":57,"{":1197,"<":25137}
closetoopen = {"]":"[","}":"{",">":"<",")":"(",}
def getscore(text):
    x = ""
    for char in text:
        if char not in closetoopen:
            x += char
        else:
            if x[-1] == closetoopen[char]:
                x = x[:-1]
            else:
                return scores[closetoopen[char]]
                
    return 0

print(sum([getscore(x) for x in data]))