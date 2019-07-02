def check(l):
        d=1
        for v in range(0,len(l)-1):
                if l[v]!=l[v+1]:
                        d=d+1
                else:
                    break
        return d
num=int(input())
l=list(map(int,input().split()))
for v in range(0,len(l)):
        if l[v]>0:
                l[v]=1
        else:
             l[v]=0
s=""
for v in range(0,len(l)):
        k=l[v::]
        s=s+str(check(k))+" "
print(s.strip())
             
