arr = []
for i in range(9):
    arr.append(int(input()))
x = sum(arr)-100
arr.sort()
for i in range(len(arr)-1):
    ans = arr[i]
    if ans >= x:
        continue
    else:
        for j in range(i+1, len(arr)):
            ans +=arr[j]
            if x==ans:
                a1 = arr[i]
                a2 = arr[j]
                break
            else:
                ans -=arr[j]
arr.remove(a1)
arr.remove(a2)
for i in arr:
    print(i)