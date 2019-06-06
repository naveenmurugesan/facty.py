b=input()
L=[]
for x in b:
	if x not in L:
		L.append(x)
	else:
		break
print(len(L))
