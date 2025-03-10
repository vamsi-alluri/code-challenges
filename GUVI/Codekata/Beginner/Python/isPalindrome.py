def reverse(s): 
    str = "" 
    for i in s:
        str = i + str
    return str
n = input()
if reverse(n)==n:
    print("yes")
else:
    print("no")
