x=int(input())
y=input().split()
l=[]
for i in range(0,x):
  if(int(y[i])==i):
    l.append(y[i])
if(l==[]):
  print("-1")
else:
  l.sort()
  for j in range(0,len(l)):
    print(l[j],end=" ")
