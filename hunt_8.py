p2=int(input())
l2=list(map(int,input().split()))
for i in range(0,p2-2):
    for j in range(i+1,p2-1):
        for k in range(j+1,p2):
            if(l2[i]+l2[j]==l2[k]):
                print(l2[i], l2[j], l2[k])
