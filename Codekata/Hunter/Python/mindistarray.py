dist=[]
def distance(n,a):
   for i in range(len(n)):
      if(a==n[i]):
         dist.append(i)
d=int(input())
n=[int(s) for s in input().split()]
a=[int(s) for s in input().split()]
distance(n,a[0])
distance(n,a[1])
print(abs(dist[0]-dist[1]))
