def find_num(value):
    row = 0
    answer= 0
    while row!=N:
        check = [1,2,3,4,5,6]
        for i in range(6):
            if arr[row][i]==value:
                check.remove(value)
                check.remove(arr[row][updown[i]])
                answer += max(check)
                value = arr[row][updown[i]]
                break
        row+=1
    return answer

max_answer = 0
updown = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0 }
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))


for i in range(6):    
    answer = find_num(arr[0][i])
    if answer>max_answer:
        max_answer = answer
print(max_answer)

    