from itertools import combinations
d,k = input().split()
k = int(k)
lis = []
f = 0
n = [int(X) for X in input().split()]
m = list(combinations(n,2))
for i in m:
    if sum(i)==k:
        f += 1
if f>=1:
    print("YES")
else:
    print("NO")
