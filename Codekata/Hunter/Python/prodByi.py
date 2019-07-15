def multi(n):
    res = 1
    for i in n:
        res = res * i
    return res
dummy = input()
n = [int(x) for x in input().split()]
mul = multi(n)
a = []
for i in n:
    a.append(str(mul//i))
print(" ".join(a))
