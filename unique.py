x=int(input())
y=[int(y) for y in input().split()]
e=[]
for i in range(0,x-1):
    for j in range(i+1,x):
        if(y[i]==y[j]):
            e.append(y[i])
            
d=list(set(sorted(e)))
if len(d)==0:
    print("unique")
else:
    for i in range(0,len(d)):
        print(d[i],end=" ")
