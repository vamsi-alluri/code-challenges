n = [int(x) for x in input().split()]
m = max(n)
a = []
for i in range(1,m+1):
    if (n[0]%i==0 and n[1]%i==0):
        a.append(i)
print(max(a))
