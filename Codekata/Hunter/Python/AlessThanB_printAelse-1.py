#75
#input 5 3 1 6 -1
#output 3 1 -1 -1 -1
#if 5>3 print 3 else -1
c = [int(x) for x in input().split()]
a = []
l = len(c)
for i in range(1,l):
    if c[i-1]>c[i]:
        a.append(str(c[i]))
    else:
        a.append(str(-1))
a.append(str(-1))
print(" ".join(a))
