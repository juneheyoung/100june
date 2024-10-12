def solution(sizes):
    answer = 0
    garo = max(sizes[0][0],sizes[0][1])
    sero = min(sizes[0][0],sizes[0][1])
    for i in sizes:
        x = i[0]
        y = i[1]
        if max(x,y)>garo:     
            garo = max(x,y)
            if min(x,y)>sero:
                sero = min(x,y)
        if min(x,y)>sero:
            sero = min(x,y)
            
    return garo*sero