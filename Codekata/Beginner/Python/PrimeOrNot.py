import math
n = int(input())
if int(math.sqrt(n))==2:
    print("yes")
else:
    f = 0
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            f=0
            break
        else:
            f=1
    if (f):
        print("yes")
    else:
        print("no")
