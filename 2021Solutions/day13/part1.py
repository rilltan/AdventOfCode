import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

points = [[int(x.split(",")[0]),int(x.split(",")[1])] for x in data if x and x[0].isdigit()]
folds = [(x[11],int(x[13:])) for x in data if x and x[0].isalpha()]

coord = {"x":0,"y":1}
fold = folds[0]
for i in range(len(points)):
    if points[i][coord[fold[0]]] > fold[1]:
        points[i][coord[fold[0]]] = 2*fold[1] - points[i][coord[fold[0]]]

points = set((x,y) for x,y in points)
prco(len(points))