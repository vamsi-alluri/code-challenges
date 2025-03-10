def func(l):
    n = 2
    c = -1
    if len(l[0])<len(l[1]):
        mini = len(l[0])
    else:
        mini = len(l[1])
    for i in range(mini):
        s = ""
        s = s + l[1][i]
        if list(set((l[0][i]))) == list(set(s)):
            if c == -1:
                c = 0
            c += 1
    return c

n,s = map(str, input().split())
l = []
if n == s:
    print(0)
elif len(n)<len(s):
    len(set([*n]))>len(set([*s])) ? print(abs(len(n))):print(abs(len(n)))
else:
    l.append(n)
    l.append(s)
    ans = func(l)
    print(ans)
    if ans == -1:
        print(len(s))
    else:
        print(abs(len(s)-ans))
    
