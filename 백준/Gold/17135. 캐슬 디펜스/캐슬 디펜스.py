import copy
from collections import defaultdict
N,M, D = map(int,input().split())

grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)

combi = []
global hit 
t_grid = copy.deepcopy(grid)
hit = 0
global answer
answer = 0

# 모든 적이 격자판에서 제외되면 게임 끝
def check_enemy():
    for i in range(N):
        for j in range(M):
            if grid[i][j] ==1:
                return False
    return True

# 궁수 위치를 받고 게임 시작
def start_game(a_combi):
    global hit 
    archer_pos_coloum = []
    for idx in a_combi:
        archer_pos_coloum.append(idx)
    #idx는 적들이 있는 grid 컬럼
    while not check_enemy():
        attacked_enemy_pos = archer_attack(archer_pos_coloum)
        enemy_move(attacked_enemy_pos)
    return hit

# 궁수 공격
def archer_attack(a_pos_c):
    global hit 
    #궁수 포지션 배치
    a_r = N
    cnt= 0
    enemy_dist_tmp = [100000] * M
    enemy_kil_pos_tmp = defaultdict(list)
    enemy_kil_pos = set()
    #밑에 부터시작
    for i in range(N-1,-1,-1):
        for j in range(M):
            #만약 적이면
            if grid[i][j] == 1:
                #거리 확인
                for k in a_pos_c:
                    dist = abs(i-a_r) + abs(j-k)
                    # D 이하이면 추가
                    if dist <= D:
                        if enemy_dist_tmp[k] > dist:
                            enemy_dist_tmp[k] = dist
                        if not enemy_kil_pos_tmp[k]:
                            enemy_kil_pos_tmp[k] = [[dist,i,j]]
                        else:
                            enemy_kil_pos_tmp[k].append([dist,i,j])
    # 추가된 적 공격가능 정보를 바탕으로 최소값인 경우 제거
    for i in a_pos_c:
        if not enemy_kil_pos_tmp.get(i):
            continue
        tt = []
        for j in enemy_kil_pos_tmp.get(i):
            #최솟값을 가지는 적 거리 저장
            if j[0] == enemy_dist_tmp[i]:
                tt.append((j[1],j[2]))
        # 만약 최솟값을 가지는 적이 2명 이상일 경우 가장 왼쪽에 있는거 제거하기위해 col이 작은 값 선택
        if len(tt) >= 2:
            tt.sort(key=lambda x:x[1])
        # 삭제 조건에 맞는 pos저장(set)
        enemy_kil_pos.add((tt[0][0], tt[0][1]))
    # 중복해서 제거할 수 있으므로 set을 통해 몇개 제거 됐는지 체크
    hit += len(enemy_kil_pos)
    return enemy_kil_pos

# 공격 종료 후 적 이동
def enemy_move(enemy_kil_pos):
    if enemy_kil_pos:
        for r,c in enemy_kil_pos:
            grid[r][c] = 0
    grid_tmp = copy.deepcopy(grid)
    # 적 옯기기
    for rr in range(1,N):
        for cc in range(M):
            grid[rr][cc] = grid_tmp[rr-1][cc]
    for i in range(M):
        grid[0][i] = 0
    
# 궁수의 위치를 랜덤으로 3개 뽑는다. 조합사용(중복 x)
def dfs(pick,idx):
    global hit
    global answer
    if pick == 3:
        answer = max(answer,start_game(combi))
        # 초기화
        hit = 0
        for i in range(N):
            for j in range(M):
                grid[i][j] = t_grid[i][j]
        return
    for i in range(idx,M):
        combi.append(i)
        dfs(pick+1, i+1)
        combi.pop()

dfs(0,0)

print(answer)