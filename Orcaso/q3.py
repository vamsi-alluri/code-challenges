l = int(input())
b = input()
n = input().split()
c = 0
for i in n:
    if i[:len(b)]==b:
        c=c+1
print(c)
