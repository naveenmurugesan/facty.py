nn,kk = map(int,input().split())
a = list(map(int,input().split()))
b,c = 0,[]
for i in range(0,len(a)):
  t = i
  for p in range(0,len(a)):
    for l in range(0,kk):
      if l == kk-1:
        try:
          b += a[p+i]
        except IndexError:
            t = t-1
            b +=a[t]
      else:
        b += a[i]
    c.append(b)
    b = 0
for i in range(0,len(a),kk):
  b = sum(a[i:i+kk])
  c.append(b)
print(*sorted(set(c)))
