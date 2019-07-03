p=int(input())
l=list(map(int,input().split()))
for i in range(0,p-2):
    for j in range(i+1,p-1):
        for k in range(j+1,p):
            if(l[i]+l[j]==l[k]):
                print(l[i], l[j], l[k])
