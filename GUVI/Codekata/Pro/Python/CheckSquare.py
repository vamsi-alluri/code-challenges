a = []
b = []
for i in range(4):
    n = [int(i) for i in input().split()]
    if i%2==0:
        a.extend(n)
    else:
        b.extend(n)
if ((abs(a[0]-a[1]) == abs(a[2]-a[3])) and (abs(b[0]-b[1]) == abs(b[2]-b[3]))):
    print("yes")
else:
    print("no")
