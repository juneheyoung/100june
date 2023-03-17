def dfs(x, y, cnt):
		global res, t
		res = max(res, cnt)
		for i in range(4):
		    nx, ny = x+dx[i], y+dy[i]
		    if 0 <= nx < r and 0 <= ny < c and alpha_lst[nx][ny] not in lst:
		        lst.add(alpha_lst[nx][ny])
		        dfs(nx, ny, cnt+1)
		        lst.remove(alpha_lst[nx][ny])    
res = 0
r, c = map(int, input().split())
alpha_lst = [list(input()) for _ in range(r)]
lst = set()    
lst.add(alpha_lst[0][0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(0, 0, 1)

print(res)