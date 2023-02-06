N, M = list(map(int,input().split()))
seq = []


def dfs():
    if len(seq)==M:
        print(' '.join(map(str,seq)))
        return
    for i in range(1,N+1):
        if i not in seq:
            if seq==[]:
                seq.append(i)
                dfs()
                seq.pop(-1)
            elif i>seq[-1]:
                seq.append(i)
                dfs()
                seq.pop(-1)
            
dfs()

