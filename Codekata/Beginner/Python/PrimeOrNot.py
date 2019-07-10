import math
n = int(input())
root_of_n = int(math.sqrt(n))
if root_of_n==2:
    print("yes")
else:
    f = 0
    for i in range(2,root_of_n):
        if n%i==0:
            f=0
            break
        else:
            f=1
    if (f):
        print("yes")
    else:
        print("no")
