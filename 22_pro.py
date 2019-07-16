    
aa=int(input())
ss=list(map(int,input().split()))
su=0
se=0
for i in range(aa):
	if i%2==0:
		su=su+ss[i]
	else:
		se+=ss[i]
print(max(su,se))
