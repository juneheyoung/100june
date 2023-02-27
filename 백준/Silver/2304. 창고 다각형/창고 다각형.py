N = int(input())
arr = []
for tc in range(1,N+1):
    a, b = map(int,input().split())
    arr.append((a,b))
arr.sort()
ans = 0
temp_x = arr[0][0]
temp_y = arr[0][1]

for i in range(1,len(arr)):
    if temp_y<=arr[i][1]:
        ans += (arr[i][0]-temp_x)*temp_y
        temp_x= arr[i][0]
        temp_y = arr[i][1]
# ans = ans+temp_y
# ans += temp2_y
if arr[len(arr)-1][1] == temp_y:
    ans+= temp_y
else:
    ans += temp_y
    temp2_x = arr[-1][0]
    temp2_y = arr[-1][1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i][0] == temp_x:
            ans+= (temp2_x-temp_x)*temp2_y
            break
        if arr[i][1]>=temp2_y:
            ans+= (temp2_x-arr[i][0])*temp2_y
            temp2_x = arr[i][0]
            temp2_y = arr[i][1]
print(ans)

