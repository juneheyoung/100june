def solution(arr):
    answer = []
    x = -1
    for i in arr:
        if i != x:
            answer.append(i)
            x = i 
    return answer