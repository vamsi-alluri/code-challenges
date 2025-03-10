dummy = input()
string = [int(x) for x in input().split()]
dic = {}
for i in string:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
mini = min(dic,key=dic.get)
print(mini)
