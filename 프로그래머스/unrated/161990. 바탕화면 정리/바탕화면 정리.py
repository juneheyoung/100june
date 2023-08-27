def solution(wallpaper):
    answer = []
    sero = len(wallpaper)
    garo = len(wallpaper[0])
    max_garo = -1
    min_garo = garo
    max_sero = -1
    min_sero = sero
    for i in range(sero):
        for j in range(garo):
            if wallpaper[i][j] =='#':
                if j>max_garo:
                    max_garo = j
                if j<min_garo:
                    min_garo = j
                if i>max_sero:
                    max_sero = i
                if i<min_sero:
                    min_sero = i
    answer = [min_sero,min_garo,max_sero+1,max_garo+1]
    return answer