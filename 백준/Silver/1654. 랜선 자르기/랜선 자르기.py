K, N = map(int,input().split())
arr = []
for ct in range(K):
    arr.append(int(input()))
def count_N(x):
    ans = 0
    for i in arr:
        ans += i//x
    return ans
start = 1
end = max(arr)
while start<=end :
    mid = (start+end)//2
    if count_N(mid)>=N:
        start =mid+1
    else:
        end = mid-1
print(end)