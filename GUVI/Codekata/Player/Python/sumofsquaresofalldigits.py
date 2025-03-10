#sum of squares of all digits
num=int(input())
temp = num
su = 0
while temp > 0:
   digit = (temp % 10) ** 2
   su += digit
   temp //= 10
print(su)
# this question is also in the hunter section
