from collections import deque
dummy,x = input().split()
x = int(x)
n = [x for x in input().split()]
d=deque(n)
d.rotate(x)
print(" ".join(d))
