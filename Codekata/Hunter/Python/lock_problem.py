n = int(input())
s = 0
j=2
for i in range(n-2,0,-1):
    s = s + (i*j)
    j=j+1
print(2*n - 1 + s)
