# problem 1
print(sum(list(map(lambda a:ord(a)-38 if a.isupper() else ord(a)-96,list(map(lambda a:a[0].intersection(a[1]).pop(),list(map(lambda a:[set(a[0:int(len(a)/2)]),set(a[int(len(a)/2)::1])],list(map(lambda a:a.strip(),open("day03.txt").readlines()))))))))))
# problem 2
print(sum(list(map(lambda a:ord(a)-38 if a.isupper() else ord(a)-96,list(map(lambda a:a[0].intersection(a[1]).intersection(a[2]).pop(),(lambda b:[[set(b[a*3]),set(b[a*3+1]),set(b[a*3+2])] for a in range(int(len(b)/3))])(list(map(lambda a:a.strip(),open("day03.txt").readlines())))))))))