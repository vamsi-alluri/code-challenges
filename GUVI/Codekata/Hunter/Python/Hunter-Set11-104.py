num=int(input())
temp = num
su = 0
a = []
while temp > 0:
   digit = (temp % 10)
   a.append(digit)
   su += sum(a)
   print("a",a," sum",su,end="")
   temp //= 10
# =============================================================================
# for (i in range(num)):
#     for(j in range(i)):
#         sum +=a[j]
# =============================================================================
print(su)