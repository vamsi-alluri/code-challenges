n = [*input()]
l = []
for i in range(1,len(n)):
    a = ""
    try:
        while(n[i].isdigit()==True):
            a = a+n[i]
            i+=1
    except IndexError:
        pass
    if a.isdigit():
        l.append(int(a))
print(max(l))
