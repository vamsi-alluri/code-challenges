dummy,q = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]
l = []
temp = []
for i in range(q):
    s = [int(x) for x in input().split()]
    l.append(s)
for i in range(q):
    lower = l[i][0]
    upper = l[i][1]
    temp = n[lower-1:upper]
    temp.sort()
    print(temp[0])
