def reverse(s): 
    str = "" 
    for i in s:
        str = i + str
    return str
result = []
n = [[x] for x in input().split()]
l = len(n)
for i in range(l):
    result.append(reverse(str("".join(n[i]))))
print(" ".join(result))
