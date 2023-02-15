import heapq
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    stack =[]
    answer = 0
    for i in arr:
        if len(stack)<2 :
            heapq.heappush(stack,i)
        elif i>=stack[1]:
            a = heapq.heappop(stack)
            b = heapq.heappop(stack)
            heapq.heappush(stack,a+b)
            answer += a+b
            heapq.heappush(stack,i)
        elif i<stack[1]:
            heapq.heappush(stack,i)
    while len(stack)>1:
        a = heapq.heappop(stack)
        b = heapq.heappop(stack)
        heapq.heappush(stack,a+b)
        answer += a+b
    print(answer)           
