N, M = list(map(int,input().split()))
seq =[]
arr = list(map(int,input().split()))
arr = sorted(arr)
def dfs():
    
    if len(seq) == M:
        print(' '.join(map(str,seq)))
        return 
    for i in arr:
        if i not in seq:
            seq.append(i)
            dfs()
            seq.pop(-1)
dfs()