n11,t=map(int,input().split())
s11=list(map(int,input().split()))
c11=0
for i in s11:
     t11=86400-i
     t=t-t11
     c11=c11+1
     if t<=0:
          break  
print(c11)
