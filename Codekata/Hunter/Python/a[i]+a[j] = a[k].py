from itertools import combinations
n = [x for x in input().split()]
comb = combinations(n,3)
n = list(sum(comp, ()))
l = len(n)
for i in range(0,l,+3):
    if ((n[i]+n[i+1])==n[i+2]):
        print(n[i],n[i+1],n[i+2])
