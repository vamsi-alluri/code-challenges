def isArmstrong (x):
    n = 0
    temp = x
    while (x!=0):
        n = n+1
        x = x/10
    sum1 = 0
    while (temp!=0):
        r = temp%10
        sum1 = sum1 + (r**3)
        temp = temp/10
    if (sum1==x):
        print("yes")
    else:
        print("no")
n = int(input())
isArmstrong(n)
