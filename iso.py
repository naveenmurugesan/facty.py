x1,x2=list(map(str,input().split()))
x=len(set(x1))
y=len(set(x2))
if x==y :
    print("yes")
else:
    print("no")
