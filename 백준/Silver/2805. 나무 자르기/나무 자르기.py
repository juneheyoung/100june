N, G = map(int,input().split())
Tree = list(map(int,input().split()))
Tree.sort()
def bin(Tree,goal):
    start = 0
    end = len(Tree)-1
    
    while start<= end:
        mid = (start+end)//2
        ans = sum(Tree[mid:])-Tree[mid]*len(Tree[mid:])
        if ans > goal:
            start = mid+1
            check = 1
        elif ans< goal:
            end = mid-1
            check=0
        else:
            return Tree[mid]
    if check ==1:
        mid = mid+1
        ans =sum(Tree[mid:])-Tree[mid]*len(Tree[mid:])
    sos = Tree[mid]
    lenth = len(Tree)-mid  # lenth 씩 커진다    
    dif = goal - ans
    xy = dif % lenth
    xx = dif // lenth
    if xy==0:
        sos = sos -xx
    else:
        sos = sos-(xx+1)
    return sos
print(bin(Tree,G))