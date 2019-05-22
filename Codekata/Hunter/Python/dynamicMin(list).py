a = [int(x) for x in input().split()]
solution = []
l = len(a)
for i in range(0,l):
    print(a[0:i+1])
    solution.append(str(min(a[0:i+1])))
print(' '.join(solution))
