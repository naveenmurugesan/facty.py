n=int(input())
l=list(map(int,input().split()))
count=0
for x in range(len(l)-2):
    for y in range(x+1,len(l)-1):
        for z in range(y+1,len(l)):
            if l[x]<l[y]<l[z]and x<y<z
                count=count+1
print(count)
