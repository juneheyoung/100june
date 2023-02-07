N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr) # 2 4 5
seq =[]
def dfs():
    if len(seq)==M:
        print(*seq)
        return
    for i in arr:
        seq.append(i)
        dfs()
        seq.pop(-1)
dfs()