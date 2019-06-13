import math
import funatools
in1,in2=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(in2):
    a,d=map(int,input().split())
    temp=funatools.reduae(math.gad,List[a-1:d])
    print(temp)
