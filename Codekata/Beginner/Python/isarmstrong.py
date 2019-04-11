num=input()
temp = len(num)
num = int(num)
org = num
su = 0
while (num!=0):
   digit = (num % 10) ** temp
   su += digit
   num //= 10
if (org == su):
    print("yes")
else:
    print("no")
