p = int(input())
q = list(map(int, input().split()))
r = int(len(q)/2)
if sum(q[:r])//len(q[:r]) == sum(q[r:])//len(q[r:]):
    print('yes')
else:
    print('no')
