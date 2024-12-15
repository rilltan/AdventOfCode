import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
inputfile = open(os.path.join(os.path.dirname(__file__),"input.txt"))
data = [a for a in inputfile.readlines()]
inputfile.close()

with open(os.path.join(os.path.dirname(__file__),"output.txt"), "w") as out_file:
    def execute(program,line,i,printmode,dir,stack):
        c = program[line][i]
        if printmode == True and c != '"':
            print(c,end="",file=out_file)
        elif c == "^":
            execute(program,line+1,i-1,printmode,-1,stack)
            execute(program,line+1,i+1,printmode,1,stack)
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
            stack.append((a+b)%16)
        elif c == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append((b-a)%16)
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
            print("=",end="",file=out_file)
        elif c=="{":
            stack[0] = (line,i)
        elif c == "}":
            execute(program,stack[0][0],stack[0][1],printmode,dir,stack)
            return
        elif c in ["A","B","C","D","E","F"]:
            stack.append(int(c,16))
        elif c == "~":
            return
        elif c == ".":
            print(hex(stack[-1]).replace("0x",""),end="",file=out_file)
            # print(stack[-1],end="",file=out_file)
        # print(c,stack,end="")
        # print()
        execute(program,line+1,i+dir,printmode,dir,stack)

    def run_program(program):
        execute(program,0,program[0].find("*"),False,-1,[(-1,-1)])
    sys.tracebacklimit=2
    sys.setrecursionlimit(100)
    # run_program(data)
    # locs = [(11,23),(3,15),(10,22)]
    locs = []
    for i,line in enumerate(data[:23]):
        for j,char in enumerate(line):
            if char != " " and char != "\n":
                locs.append((i,j))

    symbols = ['/','\\','^','+','-',':','%','$','?','.','"','n','{','}','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','~','O']
    # symbols = ['.',"/"]
    # class HiddenPrints:
    #     def __enter__(self):
    #         self._original_stdout = sys.stdout
    #         sys.stdout = open(os.devnull, 'w')

    #     def __exit__(self, exc_type, exc_val, exc_tb):
    #         sys.stdout.close()
    #         sys.stdout = self._original_stdout
    sys.tracebacklimit = 2

    success = flatten([[(loc[0],loc[1],symbol) for symbol in symbols] for loc in locs])

    for loc in locs:
        original = data[loc[0]][loc[1]]
        # with HiddenPrints():
        for symbol in symbols:
            print(f"({loc[0]},{loc[1]},{symbol})",end=": ",file=out_file)
            data[loc[0]] = data[loc[0]][:loc[1]] + symbol + data[loc[0]][loc[1]+1:]
            try:
                run_program(data)
            except:
                success.remove((loc[0],loc[1],symbol))
            print(file=out_file)

        data[loc[0]] = data[loc[0]][:loc[1]] + original + data[loc[0]][loc[1]+1:]
    # print(success)
    # print(len(success))


    # possibilities = [x for x in success]
    # # possibilities = [x for x in possibilities if x[2] != "~"]
    # # print(len(possibilities))
    # # possibilities = [(11,32,"%"),(9,32,":"),(4,29,"?"),(4,29,"/")]
    # for stuff in possibilities:
    #     original = data[stuff[0]][stuff[1]]
    #     data[stuff[0]] = data[stuff[0]][:stuff[1]] + stuff[2] + data[stuff[0]][stuff[1]+1:]
    #     print(f"######### LOC {stuff[0]} {stuff[1]} SYMBOL {stuff[2]} ########\n#####################################")
    #     run_program(data)
    #     print()
    #     data[stuff[0]] = data[stuff[0]][:stuff[1]] + original + data[stuff[0]][stuff[1]+1:]


    # 11 23
    # 10 22
    # 3 15