a=input()
l=len(a)//2
m=a[:l]
r=a[l+1:]
if(m==r):
    print("YES")
else:
    print("NO")
