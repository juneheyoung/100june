N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr =sorted(arr)
seq =[]
def dfs():
    if len(seq)==M:
        print(*seq)
        return
    for i in arr:
        if seq ==[]:
            seq.append(i)
            dfs()
            seq.pop(-1)
        elif i >=seq[-1]:
            seq.append(i)
            dfs()
            seq.pop(-1)
dfs()