x1,y1 = input().split()
x2,y2 = input().split()
x3,y3 = input().split()
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)

if (abs((x1*(y2-y3)) + (x2*(y3-y1)) + (x3*(y1-y2)))==0):
    print("yes")
else:
    print("no")
