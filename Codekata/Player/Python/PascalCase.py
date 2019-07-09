n = [str(x) for x in input().split()]
for i in range(len(n)):
    n[i] = n[i][0].upper() + n[i][1:]
print(" ".join(n))