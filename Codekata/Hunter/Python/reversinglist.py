dummy = int(input())
n = [x for x in input().split()]
n.reverse()
for i in range(dummy-1):
    print(n[i],end="->")
print(n[dummy-1])
