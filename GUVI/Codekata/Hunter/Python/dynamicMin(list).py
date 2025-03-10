dummy = input()
a = [int(x) for x in input().split()]
solution = []
l = len(a)
for i in range(l):
    solution.append(str(min(a[0:i+1])))
print(' '.join(solution))
