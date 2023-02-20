N, K = map(int,input().split())
arr = list(map(int,input().split()))

ans = sum(arr[0:K])
max_val = ans
for i in range(N-K):
    ans = ans - arr[i] + arr[i+K]
    if ans > max_val:
        max_val = ans
print(max_val)
    