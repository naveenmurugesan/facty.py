from collections import *
a = int(input())
b = [int(i) for i in input().split(' ')]
d = defaultdict(int)

found = False
for i in range(a):
    d[b[i]] += 1
    if d[b[i]] == 2:
        print(b[i])
        found = True
if not found:
    print("unique")
