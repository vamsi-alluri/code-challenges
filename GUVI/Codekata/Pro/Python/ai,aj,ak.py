n,p,q,r=map(int,input().split())
a=[int(i) for i in input().split()]
for i in range(len(ns)):
    for j in range(len(ns)):
        for k in range(len(ns)):
            if i<=j<=k:
                c = [p*a[i]+q*a[j]+r*a[k]]
print(max(c))
