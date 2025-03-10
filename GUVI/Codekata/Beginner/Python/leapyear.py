class leap:
    def isLeap(self, n):
        if (((n%4==0) and (n%100!=0)) or (n%400==0)):
            print("yes")
        else:
            print("no")
n = int(input())
l = leap()
l.isLeap(n)
