X = int(input())
dp = [0 for _ in range(X+1)]
if 1<X<4:  # 1 2 3
   answer = 1
elif X==1:
    answer =0 
else:
    dp[2]=1
    dp[3]=1
    for i in range(4,X+1):
        if i%6==0:
            dp[i]=min(dp[int(i/3)],dp[int(i/2)],dp[i-1])+1
        elif i%3==0:
            dp[i] = min(dp[int(i/3)],dp[i-1])+1
        elif i%2==0:
            dp[i]=min(dp[int(i/2)],dp[i-1])+1
        else:
            dp[i]=dp[i-1]+1
    answer = dp[-1]
print(answer)