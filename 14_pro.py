in1,in2=map(int,input().split())
in3=list(map(int,input().split()))
in=[]
in3.insert(0,0)
for j in range(input2):
     v=[]
     s1=0
     k,l=map(int,input().split())
     for i in range(k,l+1):         
         s1^=in3[i]     
     in1.append(s1)
for j in in1:
    print(j)
