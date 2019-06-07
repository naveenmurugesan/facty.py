x=int(input())
sum=0
temp=x
while temp>0:
 d=temp%10
 sum+=d**3
 temp//=10
if(x==sum):
 print("yes")
else:
 print("no")
