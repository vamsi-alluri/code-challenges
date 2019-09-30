#dummy = int(input())
n = [int(x) for x in input().split()]
for i in range(len(n)):
    if i == 0:
        la = 0
        ra = (sum(n[i+1:])//len(n[i+1:]))
    else:
        la = (sum(n[:i])//len(n[:i]))
        print(n)
        ra = (sum(n[i+1:])//len(n[i+1:]) or 1)
    if la == ra:
        print(n[i])
