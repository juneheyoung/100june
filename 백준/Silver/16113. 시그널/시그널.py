N = int(input())
arr = [[0]*(N//5) for _ in range(5)]
s = input()
for i in range(5):
    for j in range(N//5):
        if s[i*(N//5)+j] =='#':
            arr[i][j] =1
        else:
            arr[i][j] =0
i = 0
answer = []
while i<N//5:
    if i ==N//5-2 or i == N//5-1:
        if arr[0][i]==1:
            answer.append(1)
            break
        else:
            i=i+1
            continue
    if arr[0][i] ==1:
        if arr[0][i+1]==1: ## 11 이므로 이제부턴 아래만 봐라
            if arr[1][i]==1:  # 0 5 6 8 9
                if arr[3][i]==0: ### 5 9 
                    if arr[1][i+2]==1: #9 
                        answer.append(9)
                        i+=4
                        continue
                    else: #5
                        answer.append(5)
                        i+=4
                        continue
                else:  # 0 6 8 
                    if arr[1][i+2]==1:# 0 8
                        if arr[2][i+1]==1:#8
                            answer.append(8)
                            i+=4
                            continue
                        else:# 0
                            answer.append(0)
                            i+=4
                            continue
                    else:#6
                        answer.append(6)
                        i+=4
                        continue
            else:
                if arr[2][i]==0: # 7
                    answer.append(7)
                    i+=4
                    continue
                else:
                    if arr[3][i]==1:#2
                        answer.append(2)
                        i+=4
                        continue
                    else: #3
                        answer.append(3)
                        i+=4
                        continue
                
        else:# 10 ---4
            if arr[2][i+1]==1: #101
                answer.append(4)
                i=i+4
                continue
            else:# 100  - 1
                answer.append(1)
                i=i+2
                continue
    else:  # 아무것도 읎음
        i=i+1
ss = ''
for i in answer:
    ss+=str(i)
print(ss)
