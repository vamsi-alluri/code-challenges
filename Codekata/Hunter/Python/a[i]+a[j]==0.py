from itertools import combinations
dummy = input()
n = [int(x) for x in input().split()]
k = max(n)
comb = combinations(n,2)
n = list(sum(comb, ()))
l = len(n)
for i in range(0,l,2):
    if (abs(n[i]+n[i+1])<k):
        a,b = n[i],n[i+1]
        k = abs(a+b)
print(a,b)
