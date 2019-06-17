n2=int(input())
l2=list(map(int,input().split()))
for i2 in range(0,len(l2)):
    if(l2[i2]%2==0 and i2%2!=0):
            print(l2[i2],end=" ")
    elif(l2[i2]%2!=0 and i2%2==0):
            print(l2[i2],end=" ")
