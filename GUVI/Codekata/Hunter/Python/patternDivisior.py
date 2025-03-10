def pattern(n):
    s = ""
    for i in range(len(n)):
        if n[i] not in s:
            s = s + n[i]
        else:
            return s
    return n
n = input()
np = input()
c = pattern(n)
if c is not None:
    if n.count(c)>=1:
        print(n.count(c)//2)
    else:
        print(1)
