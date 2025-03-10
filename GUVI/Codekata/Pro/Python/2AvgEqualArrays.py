from itertools import combinations
n = int(input())
comb = []
l = [int(x) for x in input().split()]
for i in range(1,n+1):
    comb = comb.append(list(combinations(l,i)))
comb = list(comb)
print(comb)
