#admin
n=input()
m=input()
s=[]
for x,y in zip(n,m):
    s.append(chr(ord('a')+((ord(x)-ord('a')+ord(y)-ord('a'))%26)+1))
print("".join(s))    
