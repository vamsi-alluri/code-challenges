n=int(input())
n = n*2
for i in range(0,n,+2):
    if (i!=n):
        print(i)
        for j in range(0,i,+2):
            print(1,end=" ")        
        print()
    else:
        print(1,end="")