n = [*input()]
m = int(input())
l = []
for i in range(m):
    k = [*input()]
    l.append(k)
for i in l:
    f=0
    r= []
    r.extend(n)
    for j in i:
        if j not in r:
            f=1
            break
        else:
            r.remove(j)
            
    if f==0:
        print("YES")
    else:
        print("NO")
