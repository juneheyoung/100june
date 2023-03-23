N, K = map(int,input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1,N+1):
    a, b = map(int,input().split()) # a 무게, b 가치
    for j in range(1,K+1):
        if j<a:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j-a]+b,dp[i-1][j])
print(dp[N][K])