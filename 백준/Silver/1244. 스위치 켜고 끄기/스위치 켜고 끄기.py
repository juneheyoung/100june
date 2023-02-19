def men(x,arr):
    n = len(arr)
    nx = x
    while nx<=n:
        arr[nx-1] = (arr[nx-1]+1)%2
        nx += x
    return arr

def women(x,arr):
    n = len(arr)
    arr[x-1] = (arr[x-1]+1)%2
    i=0
    while x-i!=1 and x+i !=n:
        i+=1
        if arr[x-i-1] == arr[x+i-1]:
            arr[x-i-1] = (arr[x-i-1]+1)%2
            arr[x+i-1] = (arr[x+i-1]+1)%2
        else:
            break
    return arr

N = int(input())
arr = list(map(int,input().split()))
student = int(input())
for case in range(student):
    sex, num = map(int,input().split())
    if sex ==1:
        men(num,arr)
    else:
        women(num,arr)
for x in range(1,len(arr)+1):
    if x%20 == 0:
        print(arr[x-1], end = '\n')
    else:
        print(arr[x-1], end = ' ')