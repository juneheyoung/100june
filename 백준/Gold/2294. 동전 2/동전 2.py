n , k = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [99999]*(k+1)
dp[0]=0
for i in arr:   #1 5 12
    for j in range(1,k+1):
        if j-i>=0:
            dp[j] = min(dp[j-i]+1,dp[j])

if dp[-1]==99999:
    dp[-1]=-1            
print(dp[-1])
