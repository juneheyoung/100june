from collections import deque
def bfs(start,goal):
    queue = deque()
    queue.append(start)
    visited[start]=1
    while queue:
        x = queue.popleft()
        if x==goal:
            return count[goal]
        for i in (x-D,x+U):
            if 0<i<=F and visited[i]==0: 
                visited[i]=1
                count[i] = count[x]+1
                queue.append(i)
    if count[goal]==0:
        return 'use the stairs' 



F,S,G,U,D = map(int,input().split())
visited = [0 for _ in range(F+1)]
count = [0 for _ in range(F+1)]
answer = bfs(S,G)
print(answer)