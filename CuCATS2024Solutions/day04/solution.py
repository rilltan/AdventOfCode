import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
inputfile = open(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [a for a in inputfile.readlines()]
inputfile.close()

def execute(program,line,i,printmode,dir,stack,loc):
    c = program[line][i]
    if printmode == True and c != '"':
        print(f"{c}",end="")
    elif c == "^":
        execute(program,line+1,i-1,printmode,-1,stack,loc)
        execute(program,line+1,i+1,printmode,1,stack,loc)
        return
    elif c == '"':
        printmode = not printmode
    elif c == "/":
        dir = -1
    elif c == "\\":
        dir = 1
    elif c == ":":
        stack.append(stack[-1])
    elif c == "%":
        temp = stack[-1]
        stack[-1] = stack[-2]
        stack [-2] = temp
    elif c == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif c == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif c == "?":
        if stack[-1] == 0:
            dir = -1
        else:
            stack[-1] = stack[-1]-1
            dir = 1
    elif c == "$":
        stack.pop()
    elif c.isdigit():
        stack.append(int(c))
    elif c=="n":
        print()
    elif c=="{":
        loc = (line,i)
    elif c == "}":
        execute(program,loc[0],loc[1],printmode,dir,stack,(-1,-1))
    elif c in ["A","B","C","D","E","F"]:
        stack.append(int(c,16))
    elif c == "~":
        return
    execute(program,line+1,i+dir,printmode,dir,stack,loc)

execute(data,0,47,False,-1,[],(-1,-1))