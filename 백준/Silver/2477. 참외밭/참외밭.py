N = int(input())
arr=[]
for i in range(6):
    di, l = map(int,input().split())
    arr.append(l)
big = max(arr)
for i in range(len(arr)):
    if big==arr[i]:
        if arr[i%6]==arr[(i+2)%6]+arr[(i+4)%6] :#and arr[(i+1)%6]==arr[(i+3)%6]+arr[(i+5)%6]
            if arr[(i+1)%6]>arr[(i-1)%6]:
                print(N*(arr[i%6]*arr[(i+1)%6]-arr[(i+3)%6]*arr[(i+4)%6]))
                break
            else:
                print(N*(arr[i%6]*arr[(i-1)%6]-arr[(i+2)%6]*arr[(i+3)%6]))
                break