import sys, string, math
s1,s2 = input().split()
m1 = len(s1)
m2 = len(s2)
if m2 > m1 :
    i = 0
    while i<m1 and s1[i] == s2[i] :
        i += 1
    print(m2-i)
elif m2 == m1 :
    i = 0
    while i<m2 and s1[i] == s2[i] :
        i += 1
    print(m2-i)
else :
    i = 0
    while i<m2 and s1[i] == s2[i] :
        i += 1
    s31 = s1[i:]
    s32 = s2[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(m1-i-k)
