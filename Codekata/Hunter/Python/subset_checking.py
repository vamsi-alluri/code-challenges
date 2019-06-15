dummy = input()
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
f = 0 
for i in a1:
    if i in a2:
        f = 1
    else:
        f = 0
if f == 1:
    print("YES")
else:
    print("NO")
