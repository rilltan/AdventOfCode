import os

layout = """inputfile = open("day{}.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

for x in lines:
    
"""

for i in range(13,26):
    x = open(f"day{i}_1.py","w")
    x.writelines(layout.format(i))
    x.close()