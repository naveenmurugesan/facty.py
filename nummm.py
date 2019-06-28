m,n=map(int,input().split())
a=list(map(int,input().split()))
for x in range (1,m):
    a[x]+=a[x-1]
for x in range (n):
    s,t=map(int,input().split())
    y=a[t-1] if s==1 else a[t-1]-a[s-2]
    print(y)
