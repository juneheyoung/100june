dir = [(0,1), (1,0), (0,-1),(-1,0)]
T = int(input())
for _ in range(T):
    max_x=0
    min_x=0
    max_y=0
    min_y=0    
    s = input()
    x,y = 0,0
    dir_num = 0
    for i in s:
        if i =='F':
            x,y = x+dir[dir_num][0], y+dir[dir_num][1]
            max_x = max(max_x,x)
            min_x = min(min_x,x)
            max_y = max(max_y,y)
            min_y = min(min_y,y)
        elif i=='B':
            x,y = x-dir[dir_num][0], y-dir[dir_num][1]
            max_x = max(max_x,x)
            min_x = min(min_x,x)
            max_y = max(max_y,y)
            min_y = min(min_y,y)
        elif i=='L':
            dir_num = (dir_num-1)%4
        else:
            dir_num = (dir_num+1)%4
    # print(max_x,min_x,max_y,min_y)
    lenx = max_x-min_x
    leny = max_y-min_y
    print(lenx*leny)