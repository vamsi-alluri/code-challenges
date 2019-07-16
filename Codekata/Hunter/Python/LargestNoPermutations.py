n = [*input()]
l = []
for i in n:
    l.append(int(i))
l.sort(reverse=True)
a = []
for i in l:
    a.append(str(i))
if a == n:
    print("impossible")
else:
    print("".join(a))
