import sys
input = sys.stdin.readline
def dfs(start,cnt):
    visited[start]=1
    for i in arr[start]:
        if visited[i]==0:
            cnt = dfs(i,cnt+1)
    return cnt
T = int(input())
for _ in range(1,T+1):
    N, M = map(int,input().split())
    arr=[[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    visited[0]=1
    
    for _ in range(M):
        a, b = map(int,input().split())
        # a, b = min(a,b), max(a,b)
        arr[a].append(b)
        arr[b].append(a)

    print(dfs(1,0))