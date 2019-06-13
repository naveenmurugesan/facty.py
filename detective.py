mm=int(input())
nn=[int(i) for i in input().split()]
x=0
for i in range(mm):
	for j in range(i):
		if nn[j]<nn[i]:
			x+=nn[j]
print(x)
