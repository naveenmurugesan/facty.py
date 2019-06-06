b=input()
substring=""
f=0
op=[]
if b==b[::-1]:
  op.append(0)
for x in range(len(b)-1):
  for y in range(x+1,len(b)):
    substring=b[x:y+1]
    if substring==substring[::-1]:
      op.append(len(b)-len(substring))
     
print(min(op))
