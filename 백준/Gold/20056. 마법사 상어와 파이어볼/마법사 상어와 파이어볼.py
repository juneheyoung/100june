from collections import deque
dir = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
N, M, K = map(int,input().split())  # N*N 땅덩어리, 불덩이 M개 , K 개의 턴
stack = deque()
for i in range(M):
    stack.append(list(map(int,input().split())))
# print(stack)
answer = 0
while K!=0:
    check = {}
    dir_count = [[[] for _ in range(N)] for _ in range(N)]
    while stack:
        r,c,m,s,d = stack.popleft()
        distance=s%N
        nr = (r + dir[d][1]*distance)%N
        nc = (c + dir[d][0]*distance)%N   # 불덩어리 이동만 함 
        if (nr,nc) in check:
            check[(nr,nc)] = [x + y for x, y in zip(check[(nr,nc)],[0,0,m,s,1])]    
            dir_count[nr-1][nc-1].append(d)  # dir 방향들 1 2 1 2 이런식 추가 
        else: 
            check[(nr,nc)] = [nr,nc,m,s,1]     ## 좌표들  r,c  들 모임
            dir_count[nr-1][nc-1].append(d)
            #print(dir_count)
    for i in check:
        if check[i][4]>1:
            r,c,m,s,divide_s=check[i]
            if m//5>0:
                direction = dir_count[r-1][c-1]
                evenodd= direction[0]%2
                for comd in direction:
                    if comd%2!=evenodd:
                        d = [1,3,5,7]
                        break
                else:
                    d = [0,2,4,6]
                for oden in d:
                    stack.append([r,c,m//5,s//check[i][4],oden])
        else:
            r,c=i
            stack.append(check[i][0:4]+dir_count[r-1][c-1])
    K-=1
    if not stack:
        break
ans =0
for i in stack:
    ans +=i[2]

print(ans)