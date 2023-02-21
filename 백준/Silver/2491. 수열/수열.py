N = int(input())
arr = list(map(int,input().split()))
big = 1
max_big = 1
for i in range(len(arr)-1):
    if arr[i]<=arr[i+1]:
        big +=1
        if i == len(arr)-2:
            if big>max_big:
                max_big = big
    else:
        if big>max_big:
            max_big = big
        big = 1
small = 1
max_small = 1
for i in range(len(arr)-1):
    if arr[i]>= arr[i+1]:
        small +=1
        if i == len(arr)-2:
            if small>max_small:
                max_small=small
    else:
        if small>max_small:
            max_small = small
        small=1        
print(max(max_big,max_small))
