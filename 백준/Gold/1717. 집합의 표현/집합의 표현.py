def josang(a):
    while parent[a]!=a:
        a = parent[a]
    return a
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
parent = [i for i in range(n+1)]   
for _ in range(m):
    check, a, b = map(int,input().split())
    a, b = josang(a), josang(b)
    
    if check==0:
        if a>b:
            parent[b]=a
        else:
            parent[a]=b
    else:
        if josang(a)==josang(b):
                print('YES')
        else:
            print('NO')
