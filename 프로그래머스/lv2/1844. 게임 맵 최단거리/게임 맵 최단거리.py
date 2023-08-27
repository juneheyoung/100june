from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 10
    while queue:
        step = queue.popleft()
        x = step[0]
        y = step[1]
        for i in range(4):
            nx = x+direction[i][0]
            ny = y+direction[i][1]
            if nx == n-1 and ny == m-1 :
                return visited[y][x]-8
            if 0<=nx<n and 0<=ny<m and maps[ny][nx]==1 and visited[ny][nx]==0:
                queue.append([nx,ny])
                visited[ny][nx] = visited[y][x]+1         
    return -1