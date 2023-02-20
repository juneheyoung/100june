n = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
for i in range(n):
    a, b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j]=1
res= 0
for i in range(100):
    res += sum(arr[i])
print(res)  