a1 = int(input())
b1 = list(map(int,input().split()))
d1 = []
for i in b1:
  c1 = bin(i)
  d1.append(c1)
e1 = sorted(d1)
e1.reverse()
for i in e1:
  print(int(i,2))
