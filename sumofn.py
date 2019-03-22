class sumofn:
    def sum(self, n):
        return (sum(range(1,n+1)))
n = int(input())
s = sumofn()
print(s.sum(n))
