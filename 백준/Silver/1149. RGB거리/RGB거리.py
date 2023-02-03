house = int(input())
R,G,B = map(int,input().split())
dp = [0]*3*house
dp[0] = R
dp[1] = G 
dp[2] = B
for i in range(1,house):
    R, G, B = map(int,input().split())
    dp[3*i+0] = min(dp[3*i-2],dp[3*i-1])+R
    dp[3*i+1] = min(dp[3*i-3],dp[3*i-1])+G
    dp[3*i+2] = min(dp[3*i-3],dp[3*i-2])+B
print(min(dp[-1],dp[-2],dp[-3]))