m = [int(x) for x in input().split()]
l = len(m)
a = (float)(sum(m)/l)
print("{0:.2f}".format(a),end=" ")
if a<40:
    print("F")
elif a>=40 and a<60:
    print("E")
elif a>=60 and a<70:
    print("D")
elif a>=70 and a<80:
    print("C")
elif a>=80 and a<90:
    print("B")
elif a>=90:
    print("A")
