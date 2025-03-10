from itertools import combinations
dummy = input()
n = [int(x) for x in input().split()]
comb = combinations(n,3)
n = list(sum(comb, ()))
l = len(n)
for i in range(0,l,3):
    if ((n[i]+n[i+1])==n[i+2]):
        print(n[i],n[i+1],n[i+2])
