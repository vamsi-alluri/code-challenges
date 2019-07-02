from itertools import combinations
n,k = [int(x) for x in input().split()]
m = str(n)
l = list(combinations(m,len(m)-k))
l.sort()
print("".join(l[0]))
