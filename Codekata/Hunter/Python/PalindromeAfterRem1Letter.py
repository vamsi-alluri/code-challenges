def reverse(n):
    rev = ""
    for i in n:
        rev = i + rev
    return(rev)

n = [*input()]
m = []
m.extend(n)
for i in range(len(m)):
    m = []
