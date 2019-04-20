x, y = [x for x in input().split()]
x = int(x)
y = int(y)
c = 0
if (x>=y):
    while(x>0):
        c+=1
        x-=y
    print(c)
else:
    print(0)
