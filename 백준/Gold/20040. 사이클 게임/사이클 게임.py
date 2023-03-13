def cycle(a):
    if a!=parent[a]:
        parent[a] = cycle(parent[a])
    return parent[a]
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m = map(int,input().split())
parent = [i for i in range(n+1)]
cnt = 1
flag = 0
answer = 0
for i in range(m):
    a, b = map(int,input().split())  # i번 째 차례 1부터 시작 두점 주어짐
    if flag==1:
        continue
    a, b = cycle(a), cycle(b)
    if a==b and flag==0:
        answer = cnt
        flag=1
    cnt+=1
    if a>b:
        parent[b]=a
    else:
        parent[a]=b

print(answer)