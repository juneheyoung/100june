def solution(priorities, location):
    answer = 0
    loc = [i for i in range(len(priorities))]
    while priorities:
        max_num = max(priorities)
        x = priorities.pop(0)
        y = loc.pop(0)
        if x==max_num:
            if y==location:
                return answer+1
            answer+=1
        else:
            priorities.append(x)
            loc.append(y)
    return answer