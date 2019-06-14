string = [*input()]
result = []
for i in string:
    y = string.count(i)
    if y>1:
        pass
    else:
        result.append(i)
print("".join(result))
