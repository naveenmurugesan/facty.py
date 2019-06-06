x=input()
x=int(x)
L=[]
for i in range(0,x):  
    x1=input()
    L.append(x1)
Z=[]
for i in zip(*L):
    if i.count(i[0])==len(i): 
        Z.append(i[0])
    else:
        break
print(''.join(Z))
