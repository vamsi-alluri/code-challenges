#18 beginner
def armstrong(n):
    summ = 0
    for i in n:
        summ += (int(i)**3)
    return summ

bound1, bound2 = [int(x) for x in input().split()]
a = []
for i in range(bound1,bound2):
    if (armstrong(str(i))==i):
        a.append(str(i))
print(" ".join(a))