n=[str(s) for s in input()]
c=0
d=[]
for i in range(len(n)-1):
   if(n[i]==n[i+1]):
      c=c+1
      if(i==len(n)-2):
         c=c+1
         g=[c,n[i]]
         d.append(g)
   else:      
      c=c+1
      g=[c,n[i]]
      d.append(g)
      c=0
      if(i==len(n)-2):
         c=c+1
         g=[c,n[i+1]]
         d.append(g)
for i in d:
   if(i[0]!=1):
      print(str(i[0]),end="")
      print("*",end="")
      print(i[1],end="")
   else:
      print(i[1])
