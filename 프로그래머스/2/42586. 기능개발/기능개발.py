def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        x = 100-progresses[i]
        y = speeds[i]
        if x%y ==0:
            answer.append(x//y)
        else:
            answer.append(x//y+1)
    st = 0
    tmp = []
    for i in answer:
        if i>st:
            tmp.append(1)
            st = i
        else:
            tmp[-1]+=1
    return tmp