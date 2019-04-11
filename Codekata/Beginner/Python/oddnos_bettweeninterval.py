x,y = input().split(" ")
x=int(x)
y=int(y)
l=[]
for i in range(x+1,y):
    if (i%2!=0):
        l.append(str(i))
    else:
        pass
print(" ".join(l))
