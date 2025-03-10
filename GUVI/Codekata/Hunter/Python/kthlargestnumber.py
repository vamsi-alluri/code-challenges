a=[]
dummy,k = input().split(" ")
dummy = int(dummy)
k = int(k)
n = [int(x) for x in input().split()]
n.sort()
print(n[dummy-k])
