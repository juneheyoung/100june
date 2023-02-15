N = int(input())
arr = list(map(int,input().split()))
stack = []
count = [-1]*len(arr)
for i in range(len(arr)-1,-1,-1):
    while stack!=[]:
        if arr[i]<arr[stack[-1]]:   # stack[-1]  인덱스값임 
            count[i]=arr[stack[-1]]
            break
        else:
            stack.pop()

    stack.append(i)
print(*count)