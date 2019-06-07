from itertools import combinations
m,n=map(int,input().split())
x=len(str(m))
l=list(combinations(str(m),x-n))
l=(sorted(l))
y="".join(l[0])
print(y)
