dummy = input()
array = [int(x) for x in input().split()]
second = [int(n) for n in input().split()]
length_second = len(second)
for i in range(0,length_second):
    array.append(second[i])
    print(max(array))
