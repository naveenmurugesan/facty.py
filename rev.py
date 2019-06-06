n=int(input())
rem=0
while n!=0:
  temp=m%10
  rem=(rem*10)+temp
  n=n//10
print(rem)
