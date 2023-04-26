import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(map(int,input().split()))
MOD = 1000000007
answer = 0
for i in range(N-1):
    for j in range(i+1,N):
        answer += ((arr[j] - arr[i])*(2**(j-i-1)))%MOD
print(answer%MOD)