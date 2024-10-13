def solution(routes):
    ans = 0
    routes.sort(key = lambda x : x[1])
    print(routes)
    ep = -30001
    for i in routes:
        if ep<i[0]:
            ans+=1
            ep = i[1]
    return ans