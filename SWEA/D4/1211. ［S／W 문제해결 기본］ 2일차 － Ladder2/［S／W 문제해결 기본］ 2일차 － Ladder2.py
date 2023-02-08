dx =[-1,1,0]   #왼쪽 오른쪽 위에 
dy =[0,0,-1]
 
def dfs(start):
    count=0
    visit =[start]
    queue = [start]
    while queue:
        node = queue.pop(-1)
        y,x = node
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<100 and 0<=ny<100) and arr[ny][nx]==1 and [ny,nx] not in visit:
                x = nx
                y = ny
                queue.append([y,x])
                visit.append([y,x])
                count +=1
                break           
    return count, x
 
for tc in range(1,11):
    T = int(input())
    arr=[]
    min_val=5100
    answer = 0
    for i in range(100):
        arr.append(list(map(int,input().split())))
    for j in range(100):
        if arr[99][j]==1:
            start = [99,j]
            ans,ans_index = dfs(start)
            if ans<min_val:
                min_val = ans
                answer = ans_index
 
    print(f'#{tc} {answer}')