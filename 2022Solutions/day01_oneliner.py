# problem 1
print(max(list(map(lambda y:sum(list(map(int,y))),list(map(lambda y:y.split("\n"),"".join(open("day1.txt").readlines()).split("\n\n")))))))
# problem 2
print(sum(sorted(list(map(lambda y:sum(list(map(int,y))),list(map(lambda y:y.split("\n"),"".join(open("day1.txt").readlines()).split("\n\n"))))))[-3::1]))