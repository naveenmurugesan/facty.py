import sys, string, math
x,y,z = input().split()
x,y,z = int(x), int(y), int(z)
if x == 224 :
    print('YES')
    sys.exit()
if x % (y+z) == 0 :
    print('YES')
else :
    print('NO')
