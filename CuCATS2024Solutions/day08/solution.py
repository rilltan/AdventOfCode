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
    elif c == ".":
        print(hex(stack[-1])[2:],end="")
    # print(c,stack,end="")
    # print()
    execute(program,line+1,i+dir,printmode,dir,stack,loc)

def run_program(program):
    execute(program,0,program[0].find("*"),False,-1,[],(-1,-1))
sys.tracebacklimit=2
sys.setrecursionlimit(2000)
run_program(data)
# locs = []
# for i,line in enumerate(data[1:29]):
#     for j,char in enumerate(line):
#         if char != " " and char != "\n":
#             locs.append((i+1,j))

# this excludes hex characters
# symbols = ['/','\\','^','~','+','-',':','%','$','?','.','"','n','{','}']

# class HiddenPrints:
#     def __enter__(self):
#         self._original_stdout = sys.stdout
#         sys.stdout = open(os.devnull, 'w')

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout.close()
#         sys.stdout = self._original_stdout
# sys.tracebacklimit = 2

# success = flatten([[(loc[0],loc[1],symbol) for symbol in symbols] for loc in locs])

# for loc in locs:
#     original = data[loc[0]][loc[1]]
#     print(loc)
#     with HiddenPrints():
#         for symbol in symbols:
#             data[loc[0]] = data[loc[0]][:loc[1]] + symbol + data[loc[0]][loc[1]+1:]
#             try:
#                 run_program(data)
#             except:
#                 success.remove((loc[0],loc[1],symbol))

#         data[loc[0]] = data[loc[0]][:loc[1]] + original + data[loc[0]][loc[1]+1:]

#possibilities = [(1, 26, '~'), (2, 25, '~'), (2, 27, '/'), (3, 24, '~'), (3, 28, '~'), (4, 23, '/'), (4, 23, '~'), (4, 23, '+'), (4, 23, '-'), (4, 23, ':'), (4, 23, '%'), (4, 23, '$'), (4, 23, '.'), (4, 23, 'n'), (4, 23, '{'), (4, 27, '/'), (4, 27, '~'), (4, 27, ':'), (4, 27, '%'), (4, 27, '?'), (4, 27, '.'), (4, 27, 'n'), (4, 27, '{'), (4, 29, '/'), (4, 29, '~'), (4, 29, '?'), (5, 24, '/'), (5, 24, '~'), (5, 28, '/'), (5, 28, '~'), (5, 28, '?'), (5, 30, '~'), (6, 25, '/'), (6, 25, '~'), (6, 25, ':'), (6, 29, '~'), (6, 31, '~'), (8, 31, '/'), (9, 32, '/'), (9, 32, '~'), (9, 32, ':'), (10, 33, '\\'), (10, 33, '~'), (10, 33, '+'), (10, 33, '-'), (10, 33, ':'), (10, 33, '%'), (10, 33, '$'), (10, 33, '?'), (10, 33, '.'), (10, 33, 'n'), (10, 33, '{'), (11, 32, '~'), (11, 32, '%'), (12, 31, '\\'), (12, 31, '~'), (12, 31, '%'), (12, 31, '?'), (12, 31, '{'), (13, 30, '/'), (13, 30, '~'), (13, 30, ':'), (13, 30, '.'), (13, 30, 'n'), (13, 30, '{'), (14, 31, '/'), (14, 31, '~'), (15, 32, '/'), (15, 32, '\\'), (15, 32, '~'), (15, 32, ':'), (15, 32, '?'), (15, 32, '.'), (15, 32, 'n'), (15, 32, '{'), (16, 31, '\\'), (16, 31, '~'), (16, 31, ':'), (16, 31, '%'), (16, 33, '/'), (16, 33, '~'), (17, 30, '\\'), (17, 30, '~'), (17, 30, ':'), (17, 30, '%'), (17, 34, '/'), (17, 34, '~'), (18, 29, '\\'), (18, 29, '~'), (18, 29, ':'), (18, 29, '%'), (18, 35, '/'), (18, 35, '~'), (19, 28, '/'), (19, 28, '~'), (19, 28, ':'), (19, 28, '?'), (19, 28, '.'), (19, 28, 'n'), (19, 28, '{'), (19, 36, '/'), (19, 36, '~'), (20, 37, '~'), (20, 37, ':'), (21, 36, '~'), (24, 33, '~'), (25, 22, '/'), (25, 22, '^'), (25, 22, ':'), (25, 22, '?'), (25, 22, '.'), (25, 22, 'n'), (25, 22, '{'), (25, 32, '~'), (26, 23, '/'), (26, 31, '\\'), (26, 31, '~'), (26, 31, '{'), (27, 30, ':'), (28, 31, ':')]
#possibilities = [x for x in possibilities if x[2] != "~"]
# possibilities = [(11,32,"%"),(9,32,":"),(4,29,"?"),(4,29,"/")]
# for stuff in possibilities:
#     original = data[stuff[0]][stuff[1]]
#     data[stuff[0]] = data[stuff[0]][:stuff[1]] + stuff[2] + data[stuff[0]][stuff[1]+1:]
#     print(f"######### LOC {stuff[0]} {stuff[1]} SYMBOL {stuff[2]} ########\n################################")
#     run_program(data)
#     print()
#     print()
#     data[stuff[0]] = data[stuff[0]][:stuff[1]] + original + data[stuff[0]][stuff[1]+1:]


# 11 32 %
# 9 32 :
# 4 29 ?
# 4 29 /