import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

scores = {"(":1,"[":2,"{":3,"<":4}
closetoopen = {"]":"[","}":"{",">":"<",")":"("}
opentoclose = dict([(val,key) for key,val in closetoopen.items()])
def getcompletion(text):
    x = ""
    for char in text:
        if char not in closetoopen:
            x += char
        else:
            if x[-1] == closetoopen[char]:
                x = x[:-1]
            else:
                return ""
                
    return "".join([opentoclose[char] for char in x[::-1]])

def getscore(text):
    result = 0
    for char in text:
        result *= 5
        result += scores[closetoopen[char]]
    return result