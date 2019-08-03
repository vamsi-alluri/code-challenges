n,k = map(int,input().split())
m = [int(x) for x in input().split()]
if k in m:
    print(m.count(k))
else:
    print(0)
