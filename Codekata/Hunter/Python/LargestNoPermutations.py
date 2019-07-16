b = []
def toString(List): 
    return ''.join(List) 

def permute(a, l, r): 
    if l == r: 
        b.append(toString(a)) 
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 
string = input()
k = int(string)
l = []
n = len(string) 
a = list(string) 
permute(a, 0, n-1)
for i in b:
    l.append(int(i))
l.sort()
if k == max(l):
    print("impossible")
else:
    for i in l:
        if i<=k:
            continue
        else:
            print(i)
            break
