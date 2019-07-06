n = input()
sum_even = 0
sum_odd = 0
b = [int(x) for x in input().split()]
for i in range(n):
    if (i%2==0):
        sum_even = sum_even + b[i]
    else:
        sum_odd = sum_odd + b[i]
if sum_odd >= sum_even:
    print(sum_odd)
else:
    print(sum_even)