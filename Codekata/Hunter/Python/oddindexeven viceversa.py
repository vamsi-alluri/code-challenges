dummy = input()
output = []
n = [int(x) for x in input().split()]
for i in range(len(n)):
    if ((n[i]%2==0) and (i%2!=0)):
        output.append(str(n[i]))
    elif((int(n[i]%2!=0)) and (i%2==0)):
        output.append(str(n[i]))
print(" ".join(output))
