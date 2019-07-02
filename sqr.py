m=[]
n=[]
for i in range(4):
    m.append(input().split())
for i in range(len(m)):
    a=m[i]
    x=abs(int(a[0])-int(a[1]))
    n.append(x)
if(n[0]==n[2]) and (n[1]==n[3]):
    print("yes")
else:
    print("no")
