import sys
import math
H, W, N, M = map(int,sys.stdin.readline().split())
# 가로 N칸 또는 세로 M칸 비우고 앉아야됨
# 테이블은 W개 씩 H 행 
#  (0 < H, W, N, M ≤ 50,000) => 조건 반복문 못쓸듯

a = math.ceil(H/(N+1)) 
b = math.ceil(W/(M+1)) 
answer = a*b 
print(answer)

