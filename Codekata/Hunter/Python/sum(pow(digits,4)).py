num=input()
temp = len(num)
num = int(num)
su = 0
while (num!=0):
   digit = (num % 10) ** temp
   su += digit
   num //= 10
print(su)