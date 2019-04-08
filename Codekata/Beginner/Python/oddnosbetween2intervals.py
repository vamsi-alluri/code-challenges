#Code is to be written here
x,y = input().split()
x = int(x)
y = int(y)
for i in range(x,y):
     if(i%2==0):
         continue
     else:
         print(i)