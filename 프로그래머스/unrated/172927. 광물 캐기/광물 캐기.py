def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x

    min_n = sum * 5
    if len(minerals) > min_n:
        minerals = minerals[:min_n]
        
    min_res = [[0, 0, 0] for x in range(10)] 
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            min_res[i//5][0] += 1
        elif minerals[i] == 'iron': 
            min_res[i//5][1] += 1
        else : 
            min_res[i//5][2] += 1


    sorted_min_res = sorted(min_res, key = lambda x: (-x[0], -x[1], -x[2]))
    
    answer = 0
    for mineral in sorted_min_res:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: # dia 곡괭이
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: # iron 곡괭이
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: # stone 곡괭이
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
                
    return answer