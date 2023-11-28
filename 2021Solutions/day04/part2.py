import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
import re
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

numbers = [int(x) for x in data[0].split(",")]
data = data[1:]
boards = []
for i in range(int(len(data)/6)):
    boards.append([[int(y) for y in re.split("\s+", x)] for x in data[i*6+1:i*6+6]])

marked = []
for i in range(len(boards)):
    marked.append([[False for y in range(5)] for x in range(5)])

def findWinningBoards(markedNums):
    winners = set()
    for i in range(len(markedNums)):
        for line in markedNums[i]:
            if False not in line:
                winners.add(i)
        for j in range(5):
            if markedNums[i][0][j]==True and markedNums[i][1][j]==True and markedNums[i][2][j]==True and markedNums[i][3][j]==True and markedNums[i][4][j]==True:
                winners.add(i)
    return winners

def unmarkedSum(board, marks):
    result = 0
    for i in range(5):
        result += sum([board[i][j] for j in range(5) if not marks[i][j]])
    return result


bingonumidx = -1
flag = False
winners = findWinningBoards(marked)
while not flag:
    previouswinners = winners.copy()
    bingonumidx += 1
    for boardidx in range(len(boards)):
        for lineidx in range(5):
            for numidx in range(5):
                if boards[boardidx][lineidx][numidx] == numbers[bingonumidx]:
                    marked[boardidx][lineidx][numidx] = True
    winners = findWinningBoards(marked)
    if len(winners) >= len(boards):
        flag = True

winner = winners - previouswinners
winneridx = winner.pop()

print(unmarkedSum(boards[winneridx], marked[winneridx]) * numbers[bingonumidx])