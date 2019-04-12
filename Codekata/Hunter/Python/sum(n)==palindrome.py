num=[int(x) for x in input()]
temp =int(sum(num))
x = temp
su = 0
while temp > 0:
   digit = (temp % 10)
   su += digit
   su = su * 10
   temp //= 10
su = su//10
if (x==su):
    print("YES")
else:
    print("NO")
