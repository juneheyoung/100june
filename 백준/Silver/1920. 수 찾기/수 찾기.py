def find(x):
    start=0
    end = arr_count-1
    while start<=end:                  # 2 2 3 4 5
        mid = (start+end)//2           # 0 1 2 3 4     2 
        if x == arr[mid]:
            return 1
        elif x <arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return 0

arr_count = int(input())
arr = list(map(int,input().split()))
arr.sort()
target_count = int(input())
target_list = list(map(int,input().split()))
for i in target_list:
    if i<arr[0] or i>arr[-1]:
        print('0')
    else:
        print(find(i))