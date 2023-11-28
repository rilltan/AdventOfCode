# problem 1
print(sum([["B X","C Y","A Z","A X","B Y","C Z","C X","A Y","B Z"].index(b)+1 for b in [a.strip() for a in open("day2.txt").readlines()]]))
# problem 2
print(sum([["B X","C X","A X","A Y","B Y","C Y","C Z","A Z","B Z"].index(b)+1 for b in [a.strip() for a in open("day2.txt").readlines()]]))