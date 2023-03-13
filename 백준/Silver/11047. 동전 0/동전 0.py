N, K = map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
coin =0
for i in arr:
    coin+= K//i
    K=K-(K//i)*i
print(coin)