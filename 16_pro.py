in1=int(input())
in2=list(map(int,input().split()))
in3=[1]*in1
for i in range(in1):
    if i==0:
        if in2[i]>i[i+1]:
            i[i]=i[i]+i[i+1]
    elif i>0:
        if in2[i]>in2[i-1]:
            in3[i]=in3[i]+in3[i-1]
print(sum(in3))
