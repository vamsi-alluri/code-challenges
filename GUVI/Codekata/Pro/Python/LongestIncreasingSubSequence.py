#i think it is same as longestIncreasing SubArray
dummy = input()
prev_count = 0
n = [int(x) for x in input().split()]
count = 0
for i in range(1,len(n)):
    if n[i-1]<n[i]:
        count += 1
    else:
        if prev_count<count:
            prev_count = count
        count = 1
if prev_count>count:
    print(prev_count)
else:
    print(count)
