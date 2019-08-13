n = int(input())
po = 1
while (po<n):
    po = po * 2
if abs(po-n) == 0:
    print(0)
else:
    print(abs((po//2)-n))
