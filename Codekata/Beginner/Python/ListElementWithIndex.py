dummy = input()
n = [x for x in input().split()]
l = len(n)
for i in range(l-1):
    print(n[i],i)
print(n[l-1],i+1)
