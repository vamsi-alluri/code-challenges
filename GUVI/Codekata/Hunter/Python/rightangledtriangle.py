n=int(input())
for i in range(n,0,-1):
    if (i!=1):
        for j in range(i,0,-1):
            print(1,end=" ")        
        print()
    else:
        print(1,end="")