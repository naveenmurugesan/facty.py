aa,bb=map(str,input().split())
count=0
for i in range(0,len(aa)):
    for j in range(0,len(bb)):
        if aa[i]==bb[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
