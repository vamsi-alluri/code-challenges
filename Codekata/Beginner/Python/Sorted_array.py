#beginner 24
dummy = input()
n = [int(x) for x in input().split()]
n.sort()
for i in range(len(n)-1):
    print(n[i],end=" ")
print(n[len(n)-1])
