dummy = input()
output = []
f=1
n = [int(x) for x in input().split()]
for i in range(len(n)):
    if (i==n[i]):
        output.append(str(i))
        f=0
    else:
        if (f==0):
            pass
        else:
            f=-1
if (f==-1):
    print("-1")
else:
    print(" ".join(output))
