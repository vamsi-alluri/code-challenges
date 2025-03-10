string = [x for x in input().split()]
length = len(string)
f = 0
for i in range(length):
    if (string[i][0].isupper())==True:
        if (string[i][1].islower())==True:
            f = 1
        else:
            f = 0
        break
if f == 1:
    print("yes")
else:
    print("no")
