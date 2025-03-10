dummy = input()
a = [int(x) for x in input().split()]
b = a
b = list(set(a))
if len(a) == len(b):
    print("no repetitions")
else:
    print("repetition occurred")
    
