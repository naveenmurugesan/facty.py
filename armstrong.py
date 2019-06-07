b=int(input())
sum=0
temp=b
while temp>0:
 c=temp%10
 sum+=c**3
 temp//=10
if(b==sum):
 print("yes")
else:
 print("no")
