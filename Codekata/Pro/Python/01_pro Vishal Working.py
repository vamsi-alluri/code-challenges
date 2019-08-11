n = int(input())
l = []
mini = 9999999
res = []
for i in range(n):
    st = input()
    m = len(st)
    if mini>m:
        mini = m
    l.append(st)
for i in range(mini):
    s = ""
    for  j in range(1,n):
        s = s + l[j][i]
    if list(set((l[0][i]))) == list(set(s)):
        res.append(l[0][i])
print("".join(res))
