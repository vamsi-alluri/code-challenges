def reverse(m):
    return m[::-1]
n = input()
count = 0
a = []
if n==reverse(n):
    print(0)
else:
    for i in range(len(n)):
        for j in range(len(n),i+1,-1):
            a = n[i:j]
            if (reverse(a)==a):
                length = len(a)
                if count<length:
                    count = length
    print(len(n)-count)
