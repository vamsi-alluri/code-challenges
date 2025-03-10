import math
n = int(input())
f = 1
if n>0:
    for i in range(2,n//2):
        if n%i==0:
            f=0
            break
    if f==1:
        print("yes")
    else:
        print("no")
else:
    print("no")
