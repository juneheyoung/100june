def min_sum(a):   # 분산 * k
    answer = 0
    m = sum(a)/len(a)
    for i in a:
        answer+=(i-m)**2
    return answer/len(a)    

n, k = map(int,input().split())
arr = list(map(int,input().split()))
output = float('inf')
while k<=n:
    for i in range(n-k+1):
        a = arr[i:i+k]
        b = min_sum(a)
        if b<output:
            output = b
    k+=1
print(output**0.5)