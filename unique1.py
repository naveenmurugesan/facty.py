x=int(input())
values=list(map(int,input().split()))
for a in values:
  if(values.count(a)==1):
    print(a)
    break
