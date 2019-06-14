l = [*(input())]
for i in range(len(l)):
    l[i] = ord(l[i]) - 65
    l[i] = (65+(l[i] + 3)%26)
    l[i] = chr(l[i])
print(''.join(l))
