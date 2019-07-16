n = input()
prev = n[0]
previous = 0
if ("a" not in n) and ("b" not in n):
    print(0)
else:
    c = 1
    for i in n[1:]:
        if prev == "a":
            if i=="b":
                c+=1
            else:
                if previous>c:
                    pass
                else:
                    previous = c
                c=0
        if prev == "b":
            if i=="a":
                c+=1
            else:
                if previous>c:
                    pass
                else:
                    previous = c
                c=0
        prev=i
if previous<c:
    print(c)
else:
    print(previous)
