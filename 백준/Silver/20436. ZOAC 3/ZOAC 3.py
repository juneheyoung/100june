a, b = map(str,input().split())
s = input()
left = ['qwert','asdfg','zxcv0']
right = ['0yuiop','0hjkl0','bnm000']
def check(word):
    ans = 0
    global start_left
    global start_right
    for i in range(3):
        if word in left[i]:
            for j in range(len(left[i])):
                if word==left[i][j]:
                    ans += abs(i-start_left[0]) + abs(j-start_left[1])+1
                    start_left = (i,j)
                    return ans
        if word in right[i]:
            for j in range(len(right[i])):
                if word==right[i][j]:
                    ans+=abs(i-start_right[0]) + abs(j-start_right[1])+1
                    start_right = (i,j)
                    return ans
for i in range(3):
    if a in left[i]:
        for j in range(len(left[i])):
            if a==left[i][j]:
                start_left = (i,j)
    if b in right[i]:
        for j in range(len(right[i])):
            if b==right[i][j]:
                start_right = (i,j)

answer = 0
for word in s:
    answer +=check(word)
print(answer)

