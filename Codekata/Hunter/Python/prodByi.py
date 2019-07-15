import numpy
dummy = input()
n = [int(x) for x in input().split()]
mul = numpy.prod(n)
a = []
for i in n:
    a.append(str(mul//i))
print(" ".join(a))
