a,b = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]
res = []
for i in range(0,b):
    u,v = [int(x) for x in input().split()]
    l = n[u-1:v]
    l.sort()
    res.append(str(l[0]))
print("\n".join(res))
