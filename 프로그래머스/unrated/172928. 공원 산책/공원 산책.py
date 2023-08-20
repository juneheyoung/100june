def solution(park, routes):
    answer = []
    garo = len(park[0])
    sero = len(park)
    dicionary = {'S': [1,0],'N':[-1,0],'W': [0,-1],'E':[0,1]}
    arr = [[0 for _ in range(garo)] for _ in range(sero)]   
    for i in range(sero):
        for j in range(garo):
            if park[i][j] == 'S':
                x = i
                y = j
                break
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        step_x = x
        step_y = y
        for i in range(1,distance+1):
            step_x += dicionary[direction][0]
            step_y += dicionary[direction][1]
            if step_x >= sero or step_x <= -1 or step_y >= garo or step_y <= -1 or park[step_x][step_y] == 'X':
                flag = 1
                break
            
        if flag == 0:
            x += dicionary[direction][0] * distance
            y += dicionary[direction][1] * distance
    
    answer = [x,y]
    return answer