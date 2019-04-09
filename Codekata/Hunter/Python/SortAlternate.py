#Code is to be written here
def alter(a, n): 
    i = 0
    j = n-1      
    while (i < j):  
      
        print(arr[j], end =" ") 
        j-= 1
        print(arr[i], end =" ") 
        i+= 1
    if (n % 2 != 0): 
        print(a[i],end="")
        
        
n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
alter(arr,n)