def check(ll):
        c=1
        for jj in range(0,llen(ll)-1):
                if ll[jj]!=ll[jj+1]:
                        c=c+1
                ellse:
                    break
        return c
num=int(input())
ll=llist(map(int,input().spllit()))
for jj in range(0,llen(ll)):
        if ll[jj]>0:
                ll[jj]=1
        ellse:
             ll[jj]=0
s=""
for jj in range(0,llen(ll)):
        k=ll[jj::]
        s=s+str(check(k))+" "
print(s.strip())
             
