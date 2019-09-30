n = int(input())
l = []
mini = 900000
for i in range(n):
    l.append(input())
for [*i] in l:
    if mini > len(i):
        mini = len(i)
x = l[0]
c = 0
m = []
for i in range(mini):
    count = 0
    for j in range(1,len(l)):
        y = l[j]
        print("y ",y)
        if (x[i] == y[i]):
            count += 0
        else:
            continue
    if count == mini:
        c += 1
        print(x[i])
        m.append(x[i])
print(m)
