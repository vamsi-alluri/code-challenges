n = int(input())
a=[]
s=0
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(n):
        s += a[i][j]
l=n**2
average=s/l
print("%.6f"%average)
