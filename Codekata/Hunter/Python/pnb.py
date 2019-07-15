n,m = input().split()
n = int(n) 
k = [] 
for i in range(n): 
	j = [x for x in input().split()] 
	k.extend(list(set(j))) 
l = list(set(k)) 
o = [] 
for i in l: 
	if k.count(i)==n: 
		o.append(i) 
print(" ".join(o))