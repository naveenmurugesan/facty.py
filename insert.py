s1,s2=input().split()
su=0
if len(s1)>len(s2):
    s1,s2=s2,s1
q=0
while q<len(s1):
    su+=(ord(s2[q])-ord(s1[q]))
    q+=1
for q in range(q,len(s2)):
    su+=ord(s2[q])-ord('a')+1
print(su)
