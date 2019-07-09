#75
#input 5 3 1 6 -1
#output 3 1 -1 -1 -1
#if 5>3 print 3 else -1
c = [int(x) for x in input().split()]
a = []
l = len(c)
for i in range(1,l):
    if c[i-1]>c[i]:
        print(c[i],end=" ")
    else:
        print("-1",end=" ")
print("-1")
